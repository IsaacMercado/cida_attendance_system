from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_1 import NET_DVR_TIME
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ALARMHOST_LOG_RET(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_LOG_RET, [
    ('struLogTime', NET_DVR_TIME),
    ('sUserName', BYTE * 32),
    ('struIPAddr', NET_DVR_IPADDR),
    ('wMajorType', WORD),
    ('wMinorType', WORD),
    ('wParam', WORD),
    ('byRes', BYTE * 10),
    ('dwInfoLen', DWORD),
    ('sInfo', c_char * 11840),
])

NET_DVR_ALARMHOST_LOG_RET = struct_tagNET_DVR_ALARMHOST_LOG_RET
LPNET_DVR_ALARMHOST_LOG_RET = POINTER(struct_tagNET_DVR_ALARMHOST_LOG_RET)
tagNET_DVR_ALARMHOST_LOG_RET = struct_tagNET_DVR_ALARMHOST_LOG_RET
