from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_current import NET_DVR_CURRENT
from .net_dvr_frequency import NET_DVR_FREQUENCY
from .net_dvr_line_voltage import NET_DVR_LINE_VOLTAGE
from .net_dvr_power import NET_DVR_POWER
from .net_dvr_power_factor import NET_DVR_POWER_FACTOR
from .net_dvr_voltage import NET_DVR_VOLTAGE


class struct_tagNET_DVR_ALARMHOST_ELECTRICITY_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_ELECTRICITY_STATE, [
    ('iDCVoltage', c_int),
    ('iDCCurrent', c_int),
    ('struPhaseVoltage', NET_DVR_VOLTAGE),
    ('struLineVoltage', NET_DVR_LINE_VOLTAGE),
    ('struCurrent', NET_DVR_CURRENT * 4),
    ('iAverageCurrent', c_int),
    ('iNeutralCurrent', c_int),
    ('struActivePower', NET_DVR_POWER * 4),
    ('struReactivePower', NET_DVR_POWER * 4),
    ('struApparentPower', NET_DVR_POWER * 4),
    ('struPowerFactor', NET_DVR_POWER_FACTOR * 4),
    ('struFrequency', NET_DVR_FREQUENCY),
    ('byRes', BYTE * 128),
])

NET_DVR_ALARMHOST_ELECTRICITY_STATE = struct_tagNET_DVR_ALARMHOST_ELECTRICITY_STATE
LPNET_DVR_ALARMHOST_ELECTRICITY_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_ELECTRICITY_STATE)
tagNET_DVR_ALARMHOST_ELECTRICITY_STATE = struct_tagNET_DVR_ALARMHOST_ELECTRICITY_STATE
