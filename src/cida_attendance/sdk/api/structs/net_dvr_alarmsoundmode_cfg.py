from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMSOUNDMODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMSOUNDMODE_CFG, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwSoundMode', DWORD),
    ('byRes', BYTE * 12),
])

NET_DVR_ALARMSOUNDMODE_CFG = struct_tagNET_DVR_ALARMSOUNDMODE_CFG
LPNET_DVR_ALARMSOUNDMODE_CFG = POINTER(struct_tagNET_DVR_ALARMSOUNDMODE_CFG)
tagNET_DVR_ALARMSOUNDMODE_CFG = struct_tagNET_DVR_ALARMSOUNDMODE_CFG
