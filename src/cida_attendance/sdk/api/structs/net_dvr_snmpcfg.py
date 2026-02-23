from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SNMPCFG(Structure):
    pass

_S(struct_tagNET_DVR_SNMPCFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('wVersion', WORD),
    ('wServerPort', WORD),
    ('byReadCommunity', BYTE * 32),
    ('byWriteCommunity', BYTE * 32),
    ('byTrapHostIP', BYTE * 64),
    ('wTrapHostPort', WORD),
    ('byTrapName', BYTE * 32),
    ('byRes2', BYTE * 70),
])

NET_DVR_SNMPCFG = struct_tagNET_DVR_SNMPCFG
LPNET_DVR_SNMPCFG = POINTER(struct_tagNET_DVR_SNMPCFG)
tagNET_DVR_SNMPCFG = struct_tagNET_DVR_SNMPCFG
