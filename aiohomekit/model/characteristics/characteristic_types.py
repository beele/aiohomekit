#
# Copyright 2019 aiohomekit team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Union
import uuid


class _CharacteristicsTypes:
    """
    Translate the characteristic's UUIDs into the type description (as defined by Apple).
    E.g:
        "6D" becomes "0000006D-0000-1000-8000-0026BB765291" and translates to
        "public.hap.characteristic.position.current" or "position.current"
    Data is taken from chapter 8 of the R1 specification (page 144ff) or chapter 9 of the
    R2 specification (page 158ff).
    """

    ACCESSORY_PROPERTIES = "A6"
    ACTIVE = "B0"
    ACTIVE_IDENTIFIER = "E7"
    ADMINISTRATOR_ONLY_ACCESS = "1"
    AIR_PARTICULATE_DENSITY = "64"
    AIR_PARTICULATE_SIZE = "65"
    AIR_PURIFIER_STATE_CURRENT = "A9"
    AIR_PURIFIER_STATE_TARGET = "A8"
    AIR_QUALITY = "95"
    AUDIO_FEEDBACK = "5"
    BATTERY_LEVEL = "68"
    BRIGHTNESS = "8"
    BUTTON_EVENT = "126"
    CARBON_DIOXIDE_DETECTED = "92"
    CARBON_DIOXIDE_LEVEL = "93"
    CARBON_DIOXIDE_PEAK_LEVEL = "94"
    CARBON_MONOXIDE_DETECTED = "69"
    CARBON_MONOXIDE_LEVEL = "90"
    CARBON_MONOXIDE_PEAK_LEVEL = "91"
    CHARGING_STATE = "8F"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    CLOSED_CAPTIONS = "DD"
    COLOR_TEMPERATURE = "CE"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    CONFIGURED_NAME = "E3"
    CONTACT_STATE = "6A"
    CURRENT_HEATER_COOLER_STATE = "B1"
    TARGET_HEATER_COOLER_STATE = "B2"
    CURRENT_HUMIDIFIER_DEHUMIDIFIER_STATE = "B3"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    CURRENT_MEDIA_STATE = "E0"
    DENSITY_NO2 = "C4"
    DENSITY_OZONE = "C3"
    DENSITY_PM10 = "C7"
    DENSITY_PM25 = "C6"
    DENSITY_SO2 = "C5"
    DENSITY_VOC = "C8"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    DISPLAY_ORDER = "136"
    DOOR_STATE_CURRENT = "E"
    DOOR_STATE_TARGET = "32"
    FAN_STATE_CURRENT = "AF"
    FAN_STATE_TARGET = "BF"
    FILTER_CHANGE_INDICATION = "AC"
    FILTER_LIFE_LEVEL = "AB"
    FILTER_RESET_INDICATION = "AD"
    FIRMWARE_REVISION = "52"
    HARDWARE_REVISION = "53"
    HEATING_COOLING_CURRENT = "F"
    HEATING_COOLING_TARGET = "33"
    HORIZONTAL_TILT_CURRENT = "6C"
    HORIZONTAL_TILT_TARGET = "7B"
    HUE = "13"
    IDENTIFY = "14"
    IDENTIFIER = "E6"
    IMAGE_MIRROR = "11F"
    IMAGE_ROTATION = "11E"
    INPUT_EVENT = "73"
    IN_USE = "D2"
    IS_CONFIGURED = "D6"
    LEAK_DETECTED = "70"
    LIGHT_LEVEL_CURRENT = "6B"
    LOCK_MANAGEMENT_AUTO_SECURE_TIMEOUT = "1A"
    LOCK_MANAGEMENT_CONTROL_POINT = "19"
    LOCK_MECHANISM_CURRENT_STATE = "1D"
    LOCK_MECHANISM_LAST_KNOWN_ACTION = "1C"
    LOCK_MECHANISM_TARGET_STATE = "1E"
    LOCK_PHYSICAL_CONTROLS = "A7"
    LOGS = "1F"
    MANUFACTURER = "20"
    MODEL = "21"
    MOTION_DETECTED = "22"
    MUTE = "11A"
    NAME = "23"
    NIGHT_VISION = "11B"
    OBSTRUCTION_DETECTED = "24"
    OCCUPANCY_DETECTED = "71"
    ON = "25"
    OUTLET_IN_USE = "26"
    PAIR_SETUP = "4C"  # new for BLE, homekit spec page 57
    PAIR_VERIFY = "4E"  # new for BLE, homekit spec page 57
    PAIRING_FEATURES = "4F"  # new for BLE, homekit spec page 58
    PAIRING_PAIRINGS = "50"  # new for BLE, homekit spec page 58
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    PICTURE_MODE = "E2"
    POSITION_CURRENT = "6D"
    POSITION_HOLD = "6F"
    POSITION_STATE = "72"
    POSITION_TARGET = "7C"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    POWER_MODE_SELECTION = "E2"
    PROGRAM_MODE = "D1"
    RELATIVE_HUMIDITY_DEHUMIDIFIER_THRESHOLD = "C9"
    RELATIVE_HUMIDITY_HUMIDIFIER_THRESHOLD = "CA"
    RELATIVE_HUMIDITY_CURRENT = "10"
    RELATIVE_HUMIDITY_TARGET = "34"
    REMAINING_DURATION = "D4"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    REMOTE_KEY = "E1"
    ROTATION_DIRECTION = "28"
    ROTATION_SPEED = "29"
    SATURATION = "2F"
    SECURITY_SYSTEM_ALARM_TYPE = "8E"
    SECURITY_SYSTEM_STATE_CURRENT = "66"
    SECURITY_SYSTEM_STATE_TARGET = "67"
    SELECTED_RTP_STREAM_CONFIGURATION = "117"
    SELECTED_AUDIO_STREAM_CONFIGURATION = "128"
    SERIAL_NUMBER = "30"
    SERVICE_LABEL_INDEX = "CB"
    SERVICE_LABEL_NAMESPACE = "CD"
    SERVICE_INSTANCE_ID = (
        "e604e95d-a759-4817-87d3-aa005083a0d1".upper()
    )  # new for BLE, homekit spec page 127
    SERVICE_SIGNATURE = "A5"  # new for BLE, homekit spec page 128
    SET_DURATION = "D3"
    SETUP_DATA_STREAM_TRANSPORT = "131"
    SETUP_ENDPOINTS = "118"
    SIRI_INPUT_TYPE = "132"
    SLAT_STATE_CURRENT = "AA"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    SLEEP_DISCOVERY_MODE = "E8"
    SMOKE_DETECTED = "76"
    STATUS_ACTIVE = "75"
    STATUS_FAULT = "77"
    STATUS_JAMMED = "78"
    STATUS_LO_BATT = "79"
    STATUS_TAMPERED = "7A"
    STREAMING_STATUS = "120"
    SUPPORTED_AUDIO_CONFIGURATION = "115"
    SUPPORTED_DATA_STREAM_TRANSPORT_DATA_CONFIGURATION = "130"
    SUPPORTED_RTP_CONFIGURATION = "116"
    SUPPORTED_VIDEO_STREAM_CONFIGURATION = "114"
    SWING_MODE = "B6"
    TARGET_CONTROL_SUPPORTED_CONFIGURATION = "123"
    TARGET_CONTROL_LIST = "124"
    TARGET_HUMIDIFIER_DEHUMIDIFIER_STATE = "B4"
    # derived from https://github.com/KhaosT/HAP-NodeJS/blob/master/src/lib/gen/HomeKit-TV.ts
    TARGET_MEDIA_STATE = "137"
    TEMPERATURE_COOLING_THRESHOLD = "D"
    TEMPERATURE_CURRENT = "11"
    TEMPERATURE_HEATING_THRESHOLD = "12"
    TEMPERATURE_TARGET = "35"
    TEMPERATURE_UNITS = "36"
    TILT_CURRENT = "C1"
    TILT_TARGET = "C2"
    TYPE_SLAT = "C0"
    VALVE_TYPE = "D5"
    VERSION = "37"
    VERTICAL_TILT_CURRENT = "6E"
    VERTICAL_TILT_TARGET = "7D"
    VOLUME = "119"
    WATER_LEVEL = "B5"
    ZOOM_DIGITAL = "11D"
    ZOOM_OPTICAL = "11C"

    class Vendor:
        # Vendor specific extensions

        # Elgato Eve
        EVE_ENERGY_VOLTAGE = "E863F10A-079E-48FF-8F27-9C2605A29F52"
        EVE_ENERGY_AMPERE = "E863F126-079E-48FF-8F27-9C2605A29F52"
        EVE_ENERGY_WATT = "E863F10D-079E-48FF-8F27-9C2605A29F52"
        EVE_ENERGY_KW_HOUR = "E863F10C-079E-48FF-8F27-9C2605A29F52"

        # 0 = high, 4 = medium, 7 = low.
        EVE_MOTION_SENSITIVITY = "E863F120-079E-48FF-8F27-9C2605A29F52"
        # Persistence of motion indication in seconds
        EVE_MOTION_DURATION = "E863F12D-079E-48FF-8F27-9C2605A29F52"

        EVE_ROOM_AIR_QUALITY_PPM = "E863F10B-079E-48FF-8F27-9C2605A29F52"

        EVE_DEGREE_AIR_PRESSURE = "E863F10F-079E-48FF-8F27-9C2605A29F52"
        EVE_DEGREE_ELEVATION = "E863F130-079E-48FF-8F27-9C2605A29F52"

        # HAA - Home Accessory Architect
        # https://github.com/RavenSystem/esp-homekit-devices
        HAA_SETUP = "F0000102-0218-2017-81BF-AF2B7C833922"
        HAA_UPDATE = "F0000101-0218-2017-81BF-AF2B7C833922"

        # Koogeek
        # Watts
        KOOGEEK_REALTIME_ENERGY = "4AAAF931-0DEC-11E5-B939-0800200C9A66"
        KOOGEEK_REALTIME_ENERGY_2 = "7BBBA96E-EB2D-11E5-A837-0800200C9A66"

        # VOCOLinc
        VOCOLINC_HUMIDIFIER_SPRAY_LEVEL = "69D52519-0A4E-4898-8335-4739F9116D0A"
        VOCOLINC_HUMIDIFIER_TIMER_SETTING = "F84B3138-E44F-49B9-AA91-9E1736C247C0"
        VOCOLINC_HUMIDIFIER_COUNTDOWN = "43CE176B-2933-4034-98A7-AD215BEEBF2F"

        VOCOLINC_LIGHTBULB_LIGHT_TIMER_SETTING = "A30DFE91-271A-42A5-88BA-00E3FF5488AD"
        VOCOLINC_LIGHTBULB_LIGHT_EFFECT_MODE = "146889FC-7C42-429B-93AB-E80F79759E90"
        VOCOLINC_LIGHTBULB_LIGHT_EFFECT_FLAG = "9D4B479D-9EFB-4739-98F3-B33E6543BF7B"
        VOCOLINC_LIGHTBULB_FLASHING_MODE = "2C42B339-6EC9-4ED5-8DBF-FFCCC721B144"
        VOCOLINC_LIGHTBULB_SMOOTHING_MODE = "A3663C89-DC18-42EF-8297-910A4C0C9B61"
        VOCOLINC_LIGHTBULB_BREATHING_MODE = "6533B15C-AECB-455F-8896-20B125390F61"

        # Ecobee
        # r/o, uint8 - current mode - home(0)/sleep(1)/away(2)/temp(3)
        ECOBEE_CURRENT_MODE = "B7DDB9A3-54BB-4572-91D2-F1F5B0510F8C"
        # r/w, float - home heat temperature between 7.2 and 26.1
        ECOBEE_HOME_TARGET_HEAT = "E4489BBC-5227-4569-93E5-B345E3E5508F"
        # r/w, float - home cool temperature between 18.3 and 33.3
        ECOBEE_HOME_TARGET_COOL = "7D381BAA-20F9-40E5-9BE9-AEB92D4BECEF"
        # r/w, float - sleep heat temperature between 7.2 and 26.1
        ECOBEE_SLEEP_TARGET_HEAT = "73AAB542-892A-4439-879A-D2A883724B69"
        # r/w, float - sleep cool temperature between 18.3 and 33.3
        ECOBEE_SLEEP_TARGET_COOL = "5DA985F0-898A-4850-B987-B76C6C78D670"
        # r/w, float - away heat temp between 7.2 and 26.1
        ECOBEE_AWAY_TARGET_HEAT = "05B97374-6DC0-439B-A0FA-CA33F612D425"
        # r/w, float - away cool temp between 18.3 and 33.3
        ECOBEE_AWAY_TARGET_COOL = "A251F6E7-AC46-4190-9C5D-3D06277BDF9F"
        # w/o, uint8 - set hold schedule mode - home(0)/sleep(1)/away(2)
        ECOBEE_SET_HOLD_SCHEDULE = "1B300BC2-CFFC-47FF-89F9-BD6CCF5F2853"
        # r/w, string - 2014-01-03T00:00:00-07:00T
        ECOBEE_TIMESTAMP = "1621F556-1367-443C-AF19-82AF018E99DE"
        # w/o, bool - true to clear hold mode, false does nothing
        ECOBEE_CLEAR_HOLD = "FA128DE6-9D7D-49A4-B6D8-4E4E234DEE38"
        # r/w, 100 for on, 0 for off/auto
        # https://support.ecobee.com/s/articles/Multi-Speed-Fan-installations
        ECOBEE_FAN_WRITE_SPEED = "C35DA3C0-E004-40E3-B153-46655CDD9214"
        # r/o, Mirrors status of above
        ECOBEE_FAN_READ_SPEED = "48F62AEC-4171-4B4A-8F0E-1EEB6708B3FB"

        # ConnectSense
        # r/o, float - amps between 0 and 20
        CONNECTSENSE_ENERGY_AMPS = "00000004-0000-1000-8000-001D4B474349"
        # r/o, uint32 - state timer - in epoch format
        CONNECTSENSE_STATE_TIMER = "00000005-0000-1000-8000-001D4B474349"
        # r/o, unit32 - total amps
        CONNECTSENSE_TOTAL_AMPS = "00000006-0000-1000-8000-001D4B474349"
        # r/o, float - volts between 0 and 130
        CONNECTSENSE_ENERGY_VOLTAGE = "00000008-0000-1000-8000-001D4B474349"
        # r/o, float - amps between 0 and 20 on 20a in-wall outlet
        CONNECTSENSE_ENERGY_AMPS_20 = "00000009-0000-1000-8000-001D4B474349"
        # r/o, float - watts
        CONNECTSENSE_ENERGY_WATT = "0000000A-0000-1000-8000-001D4B474349"
        # r/o, int - power factor between 0 and 100
        CONNECTSENSE_ENERGY_POWER_FACTOR = "0000000B-0000-1000-8000-001D4B474349"
        # r/o, float - kilowatt hours between 0 and 7743802671740404396
        CONNECTSENSE_ENERGY_KW_HOUR = "0000000C-0000-1000-8000-001D4B474349"
        # r/o, string - outlet assigned name
        CONNECTSENSE_ASSIGNED_NAME = "0000000E-0000-1000-8000-001D4B474349"
        # r/o, uint32 - device type attached to outlet
        CONNECTSENSE_DEVICE_TYPE = "0000000F-0000-1000-8000-001D4B474349"

        # r/w, uint32, percentage
        AQARA_GATEWAY_VOLUME = "EE56B186-B0D3-528E-8C79-C21FC9BCF437"
        # r/w, bool
        AQARA_PAIRING_MODE = "B1C09E4C-E202-4827-B343-B0F32F727CFF"

        # r/w, uint32, percentage
        AQARA_E1_GATEWAY_VOLUME = "EE56B186-B0D3-488E-8C79-C21FC9BCF437"
        # r/w, bool
        AQARA_E1_PAIRING_MODE = "B1C09E4C-E202-4827-B863-B0F32F727CFF"

    def __init__(self) -> None:
        self.baseUUID = "-0000-1000-8000-0026BB765291"
        self._characteristics = {
            "1": "public.hap.characteristic.administrator-only-access",
            "5": "public.hap.characteristic.audio-feedback",
            "8": "public.hap.characteristic.brightness",
            "D": "public.hap.characteristic.temperature.cooling-threshold",
            "E": "public.hap.characteristic.door-state.current",
            "F": "public.hap.characteristic.heating-cooling.current",
            "10": "public.hap.characteristic.relative-humidity.current",
            "11": "public.hap.characteristic.temperature.current",
            "12": "public.hap.characteristic.temperature.heating-threshold",
            "13": "public.hap.characteristic.hue",
            "14": "public.hap.characteristic.identify",
            "1A": "public.hap.characteristic.lock-management.auto-secure-timeout",
            "1C": "public.hap.characteristic.lock-mechanism.last-known-action",
            "1D": "public.hap.characteristic.lock-mechanism.current-state",
            "1E": "public.hap.characteristic.lock-mechanism.target-state",
            "1F": "public.hap.characteristic.logs",
            "19": "public.hap.characteristic.lock-management.control-point",
            "20": "public.hap.characteristic.manufacturer",
            "21": "public.hap.characteristic.model",
            "22": "public.hap.characteristic.motion-detected",
            "23": "public.hap.characteristic.name",
            "24": "public.hap.characteristic.obstruction-detected",
            "25": "public.hap.characteristic.on",
            "26": "public.hap.characteristic.outlet-in-use",
            "28": "public.hap.characteristic.rotation.direction",
            "29": "public.hap.characteristic.rotation.speed",
            "2F": "public.hap.characteristic.saturation",
            "30": "public.hap.characteristic.serial-number",
            "32": "public.hap.characteristic.door-state.target",
            "33": "public.hap.characteristic.heating-cooling.target",
            "34": "public.hap.characteristic.relative-humidity.target",
            "35": "public.hap.characteristic.temperature.target",
            "36": "public.hap.characteristic.temperature.units",
            "37": "public.hap.characteristic.version",
            "4C": "public.hap.characteristic.pairing.pair-setup",  # new for BLE, homekit spec page 57
            "4E": "public.hap.characteristic.pairing.pair-verify",  # new for BLE, homekit spec page 57
            "4F": "public.hap.characteristic.pairing.features",  # new for BLE, homekit spec page 58
            "50": "public.hap.characteristic.pairing.pairings",  # new for BLE, homekit spec page 58
            # new for BLE, homekit spec page 127
            "e604e95d-a759-4817-87d3-aa005083a0d1".upper(): "public.hap.service.protocol.service-id",
            "52": "public.hap.characteristic.firmware.revision",
            "53": "public.hap.characteristic.hardware.revision",
            "64": "public.hap.characteristic.air-particulate.density",
            "65": "public.hap.characteristic.air-particulate.size",
            "66": "public.hap.characteristic.security-system-state.current",
            "67": "public.hap.characteristic.security-system-state.target",
            "68": "public.hap.characteristic.battery-level",
            "69": "public.hap.characteristic.carbon-monoxide.detected",
            "6A": "public.hap.characteristic.contact-state",
            "6B": "public.hap.characteristic.light-level.current",
            "6C": "public.hap.characteristic.horizontal-tilt.current",
            "6D": "public.hap.characteristic.position.current",
            "6E": "public.hap.characteristic.vertical-tilt.current",
            "6F": "public.hap.characteristic.position.hold",
            "70": "public.hap.characteristic.leak-detected",
            "71": "public.hap.characteristic.occupancy-detected",
            "72": "public.hap.characteristic.position.state",
            "73": "public.hap.characteristic.input-event",
            "75": "public.hap.characteristic.status-active",
            "76": "public.hap.characteristic.smoke-detected",
            "77": "public.hap.characteristic.status-fault",
            "78": "public.hap.characteristic.status-jammed",
            "79": "public.hap.characteristic.status-lo-batt",
            "7A": "public.hap.characteristic.status-tampered",
            "7B": "public.hap.characteristic.horizontal-tilt.target",
            "7C": "public.hap.characteristic.position.target",
            "7D": "public.hap.characteristic.vertical-tilt.target",
            "8E": "public.hap.characteristic.security-system.alarm-type",
            "8F": "public.hap.characteristic.charging-state",
            "90": "public.hap.characteristic.carbon-monoxide.level",
            "91": "public.hap.characteristic.carbon-monoxide.peak-level",
            "92": "public.hap.characteristic.carbon-dioxide.detected",
            "93": "public.hap.characteristic.carbon-dioxide.level",
            "94": "public.hap.characteristic.carbon-dioxide.peak-level",
            "95": "public.hap.characteristic.air-quality",
            "A5": "public.hap.characteristic.service-signature",
            "A6": "public.hap.characteristic.accessory-properties",
            "A7": "public.hap.characteristic.lock-physical-controls",
            "A8": "public.hap.characteristic.air-purifier.state.target",
            "A9": "public.hap.characteristic.air-purifier.state.current",
            "AA": "public.hap.characteristic.slat.state.current",
            "AB": "public.hap.characteristic.filter.life-level",
            "AC": "public.hap.characteristic.filter.change-indication",
            "AD": "public.hap.characteristic.filter.reset-indication",
            "AF": "public.hap.characteristic.fan.state.current",
            "B0": "public.hap.characteristic.active",
            "B1": "public.hap.characteristic.heater-cooler.state.current",
            "B2": "public.hap.characteristic.heater-cooler.state.target",
            "B3": "public.hap.characteristic.humidifier-dehumidifier.state.current",
            "B4": "public.hap.characteristic.humidifier-dehumidifier.state.target",
            "B5": "public.hap.characteristic.water-level",
            "B6": "public.hap.characteristic.swing-mode",
            "BF": "public.hap.characteristic.fan.state.target",
            "C0": "public.hap.characteristic.type.slat",
            "C1": "public.hap.characteristic.tilt.current",
            "C2": "public.hap.characteristic.tilt.target",
            "C3": "public.hap.characteristic.density.ozone",
            "C4": "public.hap.characteristic.density.no2",
            "C5": "public.hap.characteristic.density.so2",
            "C6": "public.hap.characteristic.density.pm25",
            "C7": "public.hap.characteristic.density.pm10",
            "C8": "public.hap.characteristic.density.voc",
            "C9": "public.hap.characteristic.relative-humidity.dehumidifier-threshold",
            "CA": "public.hap.characteristic.relative-humidity.humidifier-threshold",
            "CB": "public.hap.characteristic.service-label-index",
            "CD": "public.hap.characteristic.service-label-namespace",
            "CE": "public.hap.characteristic.color-temperature",
            "D1": "public.hap.characteristic.program-mode",
            "D2": "public.hap.characteristic.in-use",
            "D3": "public.hap.characteristic.set-duration",
            "D4": "public.hap.characteristic.remaining-duration",
            "D5": "public.hap.characteristic.valve-type",
            "D6": "public.hap.characteristic.is-configured",
            "DD": "public.hap.characteristic.closed-captions",
            "DF": "public.hap.characteristic.power-mode-selection",
            "E0": "public.hap.characteristic.current-media-state",
            "E1": "public.hap.characteristic.remote-key",
            "E2": "public.hap.characteristic.picture-mode",
            "E3": "public.hap.characteristic.configured-name",
            "E6": "public.hap.characteristic.identifier",
            "E7": "public.hap.characteristic.active-identifier",
            "E8": "public.hap.characteristic.sleep-discovery-mode",
            "114": "public.hap.characteristic.supported-video-stream-configuration",
            "115": "public.hap.characteristic.supported-audio-configuration",
            "116": "public.hap.characteristic.supported-rtp-configuration",
            "117": "public.hap.characteristic.selected-rtp-stream-configuration",
            "118": "public.hap.characteristic.setup-endpoints",
            "119": "public.hap.characteristic.volume",
            "11A": "public.hap.characteristic.mute",
            "11B": "public.hap.characteristic.night-vision",
            "11C": "public.hap.characteristic.zoom-optical",
            "11D": "public.hap.characteristic.zoom-digital",
            "11E": "public.hap.characteristic.image-rotation",
            "11F": "public.hap.characteristic.image-mirror",
            "120": "public.hap.characteristic.streaming-status",
            "123": "public.hap.characteristic.supported-target-configuration",
            "124": "public.hap.characteristic.target-list",
            "126": "public.hap.characteristic.button-event",
            "128": "public.hap.characteristic.selected-audio-stream-configuration",
            "130": "public.hap.characteristic.supported-data-stream-transport-configuration",
            "131": "public.hap.characteristic.setup-data-stream-transport",
            "132": "public.hap.characteristic.siri-input-type",
            "136": "public.hap.characteristic.display-order",
            "137": "public.hap.characteristic.target-media-state",
        }

        self._characteristics_rev = {
            self._characteristics[k]: k for k in self._characteristics.keys()
        }

    def __getitem__(self, item: Union[str, int]) -> str:
        if item in self._characteristics:
            return self._characteristics[item]

        if item in self._characteristics_rev:
            return self._characteristics_rev[item]

        # https://docs.python.org/3.5/reference/datamodel.html#object.__getitem__ say, KeyError should be raised
        raise KeyError(f"Unknown Characteristic {item}?")

    def get_short(self, uuid: str) -> str:
        """
        Returns the short type for a given UUID. That means that "0000006D-0000-1000-8000-0026BB765291" and "6D" both
        translates to "position.current" (after looking up "public.hap.characteristic.position.current").

        if item in self._characteristics:
            return self._characteristics[item].split('.', 3)[3]
        :param uuid: the UUID in long form or the shortened version as defined in chapter 5.6.1 page 72.
        :return: the textual representation
        """
        orig_item = uuid
        uuid = uuid.upper()
        if uuid.endswith(self.baseUUID):
            uuid = uuid.split("-", 1)[0]
            uuid = uuid.lstrip("0")

        if uuid in self._characteristics:
            return self._characteristics[uuid].split(".", maxsplit=3)[3]

        return f"Unknown Characteristic {orig_item}"

    def get_short_uuid(self, item_name: str) -> str:
        """
        Returns the short UUID for either a full UUID or textual characteristic type name. For information on
        full and short UUID consult chapter 5.6.1 page 72 of the specification. It also supports to pass through full
        non-HomeKit UUIDs.

        :param item_name: either the type name (e.g. "public.hap.characteristic.position.current") or the short UUID as
                          string or a HomeKit specific full UUID.
        :return: the short UUID (e.g. "6D" instead of "0000006D-0000-1000-8000-0026BB765291")
        :raises KeyError: if the input is neither a UUID nor a type name. Specific error is given in the message.
        """
        orig_item = item_name
        if item_name.upper().endswith(self.baseUUID):
            item_name = item_name.upper()
            item_name = item_name.split("-", 1)[0]
            return item_name.lstrip("0")

        if item_name.upper() in self._characteristics:
            item_name = item_name.upper()
            return item_name

        if item_name.lower() in self._characteristics_rev:
            item_name = item_name.lower()
            return self._characteristics_rev[item_name]

        try:
            uuid.UUID(f"{{{item_name}}}")
            return item_name
        except ValueError:
            raise KeyError(f"No short UUID found for Item {orig_item}")

    def get_uuid(self, item_name: str) -> str:
        """
        Returns the full length UUID for either a shorted UUID or textual characteristic type name. For information on
        full and short UUID consult chapter 5.6.1 page 72 of the specification. It also supports to pass through full
        HomeKit UUIDs.

        Shorted UUID means also leading zeros are stripped.

        :param item_name: either the type name (e.g. "public.hap.characteristic.position.current") or the short UUID or
                          a HomeKit specific full UUID.
        :return: the full UUID (e.g. "0000006D-0000-1000-8000-0026BB765291")
        :raises KeyError: if the input is neither a short UUID nor a type name. Specific error is given in the message.
        """
        orig_item = item_name
        # if we get a full length uuid with the proper base and a known short one, this should also work.
        if item_name.upper().endswith(self.baseUUID):
            item_name = item_name.upper()
            item_name = item_name.split("-", 1)[0]
            item_name = item_name.lstrip("0")

        if item_name.lower() in self._characteristics_rev:
            short = self._characteristics_rev[item_name.lower()]
        elif item_name.upper() in self._characteristics:
            short = item_name.upper()
        else:
            if len(orig_item) == 36:
                return orig_item.upper()
            raise KeyError(f"No UUID found for Item {orig_item}")

        medium = "0" * (8 - len(short)) + short
        long = medium + self.baseUUID
        return long


#
#   Have a singleton to avoid overhead
#
CharacteristicsTypes = _CharacteristicsTypes()
