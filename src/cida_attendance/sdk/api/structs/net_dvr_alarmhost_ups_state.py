from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_current import NET_DVR_CURRENT
from .net_dvr_frequency import NET_DVR_FREQUENCY
from .net_dvr_load_factor import NET_DVR_LOAD_FACTOR
from .net_dvr_power import NET_DVR_POWER
from .net_dvr_voltage import NET_DVR_VOLTAGE


class struct_tagNET_DVR_ALARMHOST_UPS_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_UPS_STATE, [
    ('struInputVoltage', NET_DVR_VOLTAGE),
    ('struBypassVoltage', NET_DVR_VOLTAGE),
    ('struOutputVoltage', NET_DVR_VOLTAGE),
    ('iRectifierVol', c_int),
    ('iInverterVol', c_int),
    ('struInputCurrent', NET_DVR_CURRENT),
    ('struBypassCurrent', NET_DVR_CURRENT),
    ('struOutputCurrent', NET_DVR_CURRENT),
    ('iInverterCurrent', c_int),
    ('struInputFrequency', NET_DVR_FREQUENCY),
    ('struBypassFrequency', NET_DVR_FREQUENCY),
    ('struOutputFrequency', NET_DVR_FREQUENCY),
    ('iInverterFre', c_int),
    ('struInputPower', NET_DVR_POWER),
    ('struBypassPower', NET_DVR_POWER),
    ('struOutputPower', NET_DVR_POWER),
    ('struComplexPower', NET_DVR_POWER),
    ('iNormalPower', c_int),
    ('iPowerFacter', c_int),
    ('struBatteryLoadFactor', NET_DVR_LOAD_FACTOR),
    ('iBatteryEstimated', c_int),
    ('iBatteryTemperature', c_int),
    ('iBatteryVoltage', c_int),
    ('byRectifierState', BYTE),
    ('byInverterState', BYTE),
    ('byChargeState', BYTE),
    ('byBatteryState', BYTE),
    ('byAutoBypassState', BYTE),
    ('byRes2', BYTE * 247),
])

NET_DVR_ALARMHOST_UPS_STATE = struct_tagNET_DVR_ALARMHOST_UPS_STATE
LPNET_DVR_ALARMHOST_UPS_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_UPS_STATE)
tagNET_DVR_ALARMHOST_UPS_STATE = struct_tagNET_DVR_ALARMHOST_UPS_STATE
