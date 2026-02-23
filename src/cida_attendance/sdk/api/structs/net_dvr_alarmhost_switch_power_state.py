from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_current import NET_DVR_CURRENT
from .net_dvr_voltage import NET_DVR_VOLTAGE


class struct_tagNET_DVR_ALARMHOST_SWITCH_POWER_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_SWITCH_POWER_STATE, [
    ('struACVoltage', NET_DVR_VOLTAGE),
    ('iDCConvertVoltage', c_int),
    ('struACCurrent', NET_DVR_CURRENT),
    ('iTotalCurrent', c_int),
    ('iBattery1Temperature', c_int),
    ('iBattery2Temperature', c_int),
    ('iBattery1Current', c_int),
    ('iBattery2Current', c_int),
    ('iBattery3Current', c_int),
    ('iBattery4Current', c_int),
    ('iBatteryTestVoltage', c_int),
    ('iRectifierOutputVoltage', c_int),
    ('iRectifierOutputCurrent', c_int),
    ('iDCOutputVoltage', c_int),
    ('byRes', BYTE * 432),
])

NET_DVR_ALARMHOST_SWITCH_POWER_SUPPLY_STATE = struct_tagNET_DVR_ALARMHOST_SWITCH_POWER_STATE
LPNET_DVR_ALARMHOST_SWITCH_POWER_SUPPLY_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_SWITCH_POWER_STATE)
tagNET_DVR_ALARMHOST_SWITCH_POWER_STATE = struct_tagNET_DVR_ALARMHOST_SWITCH_POWER_STATE
