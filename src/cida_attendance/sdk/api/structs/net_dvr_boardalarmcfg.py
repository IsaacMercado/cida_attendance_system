from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .anon_7 import NET_DVR_HANDLEEXCEPTION_V30


class struct_tagNET_DVR_BOARDALARMCFG(Structure):
    pass

_S(struct_tagNET_DVR_BOARDALARMCFG, [
    ('byEnablePullAlarm', BYTE),
    ('byRes1', BYTE * 3),
    ('struBoardHandleType', NET_DVR_HANDLEEXCEPTION_V30),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byRes2', BYTE * 32),
])

NET_DVR_BOARDALARMCFG = struct_tagNET_DVR_BOARDALARMCFG
LPNET_DVR_BOARDALARMCFG = POINTER(struct_tagNET_DVR_BOARDALARMCFG)
tagNET_DVR_BOARDALARMCFG = struct_tagNET_DVR_BOARDALARMCFG
