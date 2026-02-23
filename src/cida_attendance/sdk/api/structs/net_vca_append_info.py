from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_VCA_APPEND_INFO(Structure):
    pass

_S(struct_tagNET_VCA_APPEND_INFO, [
    ('dwSize', DWORD),
    ('dwAppendPicLen', DWORD),
    ('pAppendPicBuff', POINTER(BYTE)),
    ('byAppendPicType', BYTE),
    ('byUID', BYTE * 64),
    ('byRes1', BYTE * 3),
    ('dwTargetSpeed', DWORD),
    ('dwTargetDistance', DWORD),
    ('byAlarmType', BYTE),
    ('byRadarChannel', BYTE),
    ('byRes2', BYTE),
    ('byAppendChannelType', BYTE),
    ('dwAppendChannel', DWORD),
    ('byRes', BYTE * 44),
])

NET_VCA_APPEND_INFO = struct_tagNET_VCA_APPEND_INFO
LPNET_VCA_APPEND_INFO = POINTER(struct_tagNET_VCA_APPEND_INFO)
tagNET_VCA_APPEND_INFO = struct_tagNET_VCA_APPEND_INFO
