from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_400 import NET_DVR_WIND_SPEED_STATE
from .anon_401 import NET_DVR_GENERATE_OUTPUT_STATE
from .anon_402 import NET_DVR_SOAK_STATE
from .anon_403 import NET_DVR_SOLAR_POWER_STATE
from .anon_404 import NET_DVR_SF6_ALARMHOST_STATE
from .anon_405 import NET_DVR_WEIGHT_STATE
from .anon_406 import NET_DVR_WEATHER_STATION_STATE
from .anon_407 import NET_DVR_WATER_QLT_STATE
from .anon_408 import NET_DVR_FUEL_GAS_DETE_STATE
from .net_dvr_alarmhost_aircondition_state import NET_DVR_ALARMHOST_AIRCONDITION_STATE
from .net_dvr_alarmhost_dustnoise_sensor import NET_DVR_ALARMHOST_DUSTNOISE_SENSOR
from .net_dvr_alarmhost_electricity_state import NET_DVR_ALARMHOST_ELECTRICITY_STATE
from .net_dvr_alarmhost_environmental_logger import (
    NET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER,
)
from .net_dvr_alarmhost_gas_detector_state import NET_DVR_ALARMHOST_GAS_DETECTOR_STATE
from .net_dvr_alarmhost_switch_power_state import (
    NET_DVR_ALARMHOST_SWITCH_POWER_SUPPLY_STATE,
)
from .net_dvr_alarmhost_temp_humi_sensor_state import (
    NET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE,
)
from .net_dvr_alarmhost_transformer_temp_state import (
    NET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE,
)
from .net_dvr_alarmhost_ups_state import NET_DVR_ALARMHOST_UPS_STATE
from .net_dvr_alarmhost_waterlevel_sensor import NET_DVR_ALARMHOST_WATERLEVEL_SENSOR
from .net_dvr_fire_alarm_status import NET_DVR_FIRE_ALARM_STATUS


class union_tagNET_DVR_EXTERNAL_DEVICE_STATE_UNION(Union):
    pass

_S(union_tagNET_DVR_EXTERNAL_DEVICE_STATE_UNION, [
    ('struUpsState', NET_DVR_ALARMHOST_UPS_STATE),
    ('struSwitchPowerState', NET_DVR_ALARMHOST_SWITCH_POWER_SUPPLY_STATE),
    ('struGasDetectorState', NET_DVR_ALARMHOST_GAS_DETECTOR_STATE),
    ('struTempHumiSensorState', NET_DVR_ALARMHOST_TEMP_HUMI_SENSOR_STATE),
    ('struAirConditionState', NET_DVR_ALARMHOST_AIRCONDITION_STATE),
    ('struElectricityState', NET_DVR_ALARMHOST_ELECTRICITY_STATE),
    ('struTransformerTempState', NET_DVR_ALARMHOST_TRANSFORMER_TEMP_STATE),
    ('struWaterLevelSensor', NET_DVR_ALARMHOST_WATERLEVEL_SENSOR),
    ('struDustNoiseSensor', NET_DVR_ALARMHOST_DUSTNOISE_SENSOR),
    ('struEnvironmentLogger', NET_DVR_ALARMHOST_ENVIRONMENTAL_LOGGER),
    ('struWindSpeedState', NET_DVR_WIND_SPEED_STATE),
    ('struGenerateOutputState', NET_DVR_GENERATE_OUTPUT_STATE),
    ('struSoakState', NET_DVR_SOAK_STATE),
    ('struSolarPowerState', NET_DVR_SOLAR_POWER_STATE),
    ('struSF6AlarmHostState', NET_DVR_SF6_ALARMHOST_STATE),
    ('struWeightState', NET_DVR_WEIGHT_STATE),
    ('struWeatherStationState', NET_DVR_WEATHER_STATION_STATE),
    ('struWaterQltState', NET_DVR_WATER_QLT_STATE),
    ('struFuelGasDeteState', NET_DVR_FUEL_GAS_DETE_STATE),
    ('struFireAlarmStatus', NET_DVR_FIRE_ALARM_STATUS),
    ('byRes', BYTE * 512),
])

NET_DVR_EXTERNAL_DEVICE_STATE_UNION = union_tagNET_DVR_EXTERNAL_DEVICE_STATE_UNION
LPNET_DVR_EXTERNAL_DEVICE_STATE_UNION = POINTER(union_tagNET_DVR_EXTERNAL_DEVICE_STATE_UNION)
tagNET_DVR_EXTERNAL_DEVICE_STATE_UNION = union_tagNET_DVR_EXTERNAL_DEVICE_STATE_UNION
