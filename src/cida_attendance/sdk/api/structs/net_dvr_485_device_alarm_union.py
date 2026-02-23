from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_alarmhost_gas_detect_sys_alarminfo import (
    NET_DVR_ALARMHOST_GAS_DETECT_SYS_ALARMINFO,
)
from .net_dvr_alarmhost_switch_power_supply_alarminfo import (
    NET_DVR_ALARMHOST_SWITCH_POWER_SUPPLY_ALARMINFO,
)
from .net_dvr_alarmhost_temp_humidity_sensor_alarminfo import (
    NET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_ALARMINFO,
)
from .net_dvr_alarmhost_ups_alarminfo import NET_DVR_ALARMHOST_UPS_ALARMINFO


class union_tagNET_DVR_485_DEVICE_ALARM_UNION(Union):
    pass

_S(union_tagNET_DVR_485_DEVICE_ALARM_UNION, [
    ('struUPSAlarm', NET_DVR_ALARMHOST_UPS_ALARMINFO),
    ('struSwitchPowerAlarm', NET_DVR_ALARMHOST_SWITCH_POWER_SUPPLY_ALARMINFO),
    ('struGasDetectSystemAlarm', NET_DVR_ALARMHOST_GAS_DETECT_SYS_ALARMINFO),
    ('struTempHumiditySensorAlarm', NET_DVR_ALARMHOST_TEMP_HUMIDITY_SENSOR_ALARMINFO),
    ('byRes', BYTE * 72),
])

NET_DVR_485_DEVICE_ALARM_UNION = union_tagNET_DVR_485_DEVICE_ALARM_UNION
LPNET_DVR_485_DEVICE_ALARM_UNION = POINTER(union_tagNET_DVR_485_DEVICE_ALARM_UNION)
tagNET_DVR_485_DEVICE_ALARM_UNION = union_tagNET_DVR_485_DEVICE_ALARM_UNION
