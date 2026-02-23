from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_403(Structure):
    pass

_S(struct_anon_403, [
    ('iChangerVolInput', c_int),
    ('iChangerCurInput', c_int),
    ('iChangerPwInput', c_int),
    ('iChangerVolOutput', c_int),
    ('iChangerCurOutput', c_int),
    ('iChangerPwOutput', c_int),
    ('iDischangerVolOutput', c_int),
    ('iDischangerCurOutput', c_int),
    ('iDischangerPwOutput', c_int),
    ('iDevTemperatrue', c_int),
    ('byBatteryVolState', BYTE),
    ('byBatteryTmpState', BYTE),
    ('byChangerVolInputState', BYTE),
    ('byChangerRunState', BYTE),
    ('byChangerChgState', BYTE),
    ('byBatteryVolFlt', BYTE),
    ('byBatteryTmpFlt', BYTE),
    ('byBatteryResistanceFlt', BYTE),
    ('byVolRcgFlt', BYTE),
    ('byChangerVolInputFlt', BYTE),
    ('byChangerMosShort', BYTE),
    ('byChangerAntiOrMosShort', BYTE),
    ('byChangerAntiShort', BYTE),
    ('byInputOverCur', BYTE),
    ('byLoadOverCur', BYTE),
    ('byLoadShort', BYTE),
    ('byLoadMosShort', BYTE),
    ('byChangerFlt', BYTE),
    ('byRes', BYTE * 454),
])

NET_DVR_SOLAR_POWER_STATE = struct_anon_403
LPNET_DVR_SOLAR_POWER_STATE = POINTER(struct_anon_403)
