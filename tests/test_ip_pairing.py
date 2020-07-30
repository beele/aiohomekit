import asyncio

import pytest

from aiohomekit import exceptions


async def test_list_accessories(pairing):
    accessories = await pairing.list_accessories_and_characteristics()
    assert accessories[0]["aid"] == 1
    assert accessories[0]["services"][0]["iid"] == 1

    char = accessories[0]["services"][0]["characteristics"][0]
    print(char)
    assert char["description"] == "Identify"
    assert char["iid"] == 2
    assert char["format"] == "bool"
    assert char["perms"] == ["pw"]
    assert char["type"] == "00000014-0000-1000-8000-0026BB765291"


async def test_connection_timeout(monkeypatch, pairing):
    loop = asyncio.get_event_loop()

    # Test disconnect due to timeout
    async def connect_timeout(*args, **kwargs):
        await asyncio.sleep(20)

    monkeypatch.setattr(loop, "create_connection", connect_timeout)

    with pytest.raises(exceptions.AccessoryDisconnectedError):
        await pairing._ensure_connected(_timeout=0.1)


async def test_get_characteristics(pairing):
    characteristics = await pairing.get_characteristics([(1, 9)])

    assert characteristics[(1, 9)] == {"value": False}


async def test_get_characteristics_after_failure(pairing):
    characteristics = await pairing.get_characteristics([(1, 9)])

    assert characteristics[(1, 9)] == {"value": False}

    pairing.connection.transport.close()

    characteristics = await pairing.get_characteristics([(1, 9)])

    assert characteristics[(1, 9)] == {"value": False}


async def test_put_characteristics(pairing):
    characteristics = await pairing.put_characteristics([(1, 9, True)])

    assert characteristics == {}

    characteristics = await pairing.get_characteristics([(1, 9)])

    assert characteristics[(1, 9)] == {"value": True}


async def test_subscribe(pairing):
    assert pairing.subscriptions == set()

    await pairing.subscribe([(1, 9)])

    assert pairing.subscriptions == set(((1, 9),))

    characteristics = await pairing.get_characteristics([(1, 9)], include_events=True)

    assert characteristics == {(1, 9): {"ev": True, "value": False}}


async def test_unsubscribe(pairing):
    await pairing.subscribe([(1, 9)])

    assert pairing.subscriptions == set(((1, 9),))

    characteristics = await pairing.get_characteristics([(1, 9)], include_events=True)

    assert characteristics == {(1, 9): {"ev": True, "value": False}}

    await pairing.unsubscribe([(1, 9)])

    assert pairing.subscriptions == set()

    characteristics = await pairing.get_characteristics([(1, 9)], include_events=True)

    assert characteristics == {(1, 9): {"ev": False, "value": False}}


async def test_dispatcher_connect(pairing):
    assert pairing.listeners == set()

    def callback(x):
        pass

    cancel = pairing.dispatcher_connect(callback)
    assert pairing.listeners == set((callback,))

    cancel()
    assert pairing.listeners == set()


async def test_receiving_events(pairings):
    """
    Test that can receive events when change happens in another session.

    We set up 2 controllers both with active secure sessions. One
    subscribes and then other does put() calls.

    This test is currently skipped because accessory server doesnt
    support events.
    """
    left, right = pairings

    event_value = None
    ev = asyncio.Event()

    def handler(data):
        print(data)
        nonlocal event_value
        event_value = data
        ev.set()

    # Set where to send events
    right.dispatcher_connect(handler)

    # Set what events to get
    await right.subscribe([(1, 9)])

    # Trigger an event by writing a change on the other connection
    await left.put_characteristics([(1, 9, True)])

    # Wait for event to be received for up to 5s
    await asyncio.wait_for(ev.wait(), 5)

    assert event_value == {(1, 9): {"value": True}}


async def test_list_pairings(pairing):
    pairings = await pairing.list_pairings()
    assert pairings == [
        {
            "controllerType": "admin",
            "pairingId": "decc6fa3-de3e-41c9-adba-ef7409821bfc",
            "permissions": 1,
            "publicKey": "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed8",
        }
    ]


async def test_add_pairings(pairing):
    await pairing.add_pairing(
        "decc6fa3-de3e-41c9-adba-ef7409821bfe",
        "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed7",
        "User",
    )

    pairings = await pairing.list_pairings()
    assert pairings == [
        {
            "controllerType": "admin",
            "pairingId": "decc6fa3-de3e-41c9-adba-ef7409821bfc",
            "permissions": 1,
            "publicKey": "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed8",
        },
        {
            "controllerType": "regular",
            "pairingId": "decc6fa3-de3e-41c9-adba-ef7409821bfe",
            "permissions": 0,
            "publicKey": "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed7",
        },
    ]


async def test_add_and_remove_pairings(pairing):
    await pairing.add_pairing(
        "decc6fa3-de3e-41c9-adba-ef7409821bfe",
        "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed7",
        "User",
    )

    pairings = await pairing.list_pairings()
    assert pairings == [
        {
            "controllerType": "admin",
            "pairingId": "decc6fa3-de3e-41c9-adba-ef7409821bfc",
            "permissions": 1,
            "publicKey": "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed8",
        },
        {
            "controllerType": "regular",
            "pairingId": "decc6fa3-de3e-41c9-adba-ef7409821bfe",
            "permissions": 0,
            "publicKey": "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed7",
        },
    ]

    await pairing.remove_pairing("decc6fa3-de3e-41c9-adba-ef7409821bfe")

    pairings = await pairing.list_pairings()
    assert pairings == [
        {
            "controllerType": "admin",
            "pairingId": "decc6fa3-de3e-41c9-adba-ef7409821bfc",
            "permissions": 1,
            "publicKey": "d708df2fbf4a8779669f0ccd43f4962d6d49e4274f88b1292f822edc3bcf8ed8",
        }
    ]


async def test_identify(pairing):
    identified = await pairing.identify()
    assert identified is True
