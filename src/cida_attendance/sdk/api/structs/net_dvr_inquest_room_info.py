from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_315 import union_anon_315


class struct_tagNET_DVR_INQUEST_ROOM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_ROOM_INFO, [
    ('szCDName', c_char * 32),
    ('uCalcMode', union_anon_315),
    ('byCalcType', BYTE),
    ('byAutoDelRecord', BYTE),
    ('byAlarmThreshold', BYTE),
    ('byInquestChannelResolution', BYTE),
    ('byAutoOpenTray', BYTE),
    ('byCDPrintEnabled', BYTE),
    ('byRes', BYTE * 9),
])

NET_DVR_INQUEST_ROOM_INFO = struct_tagNET_DVR_INQUEST_ROOM_INFO
LPNET_DVR_INQUEST_ROOM_INFO = POINTER(struct_tagNET_DVR_INQUEST_ROOM_INFO)
tagNET_DVR_INQUEST_ROOM_INFO = struct_tagNET_DVR_INQUEST_ROOM_INFO
