from ctypes import Structure, c_int

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_DVR_TEMPERATUREALARMCFG(Structure):
    pass

_S(struct_tagNET_DVR_TEMPERATUREALARMCFG, [
    ('byEnableTemperatureAlarm', BYTE),
    ('byRes1', BYTE * 3),
    ('iTemperatureUpLimited', c_int),
    ('iTemperatureDownLimited', c_int),
    ('struTempHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRes2', BYTE * 32),
])

NET_DVR_TEMPERATUREALARMCFG = struct_tagNET_DVR_TEMPERATUREALARMCFG
LPNET_DVR_TEMPERATUREALARMCFG = POINTER(struct_tagNET_DVR_TEMPERATUREALARMCFG)
tagNET_DVR_TEMPERATUREALARMCFG = struct_tagNET_DVR_TEMPERATUREALARMCFG
