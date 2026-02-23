from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_230 import union_anon_230


class struct_tagNET_DVR_SLAVECAMERA_CFG(Structure):
    pass

_S(struct_tagNET_DVR_SLAVECAMERA_CFG, [
    ('dwSize', DWORD),
    ('byAddressType', BYTE),
    ('wPort', WORD),
    ('byLoginStatus', BYTE),
    ('unionServer', union_anon_230),
    ('szUserName', BYTE * 32),
    ('szPassWord', BYTE * 16),
    ('byRes1', BYTE * 128),
])

NET_DVR_SLAVECAMERA_CFG = struct_tagNET_DVR_SLAVECAMERA_CFG
LPNET_DVR_SLAVECAMERA_CFG = POINTER(struct_tagNET_DVR_SLAVECAMERA_CFG)
tagNET_DVR_SLAVECAMERA_CFG = struct_tagNET_DVR_SLAVECAMERA_CFG
