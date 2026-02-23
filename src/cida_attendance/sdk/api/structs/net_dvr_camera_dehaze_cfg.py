from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAMERA_DEHAZE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CAMERA_DEHAZE_CFG, [
    ('dwSize', DWORD),
    ('byDehazeMode', BYTE),
    ('byLevel', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_CAMERA_DEHAZE_CFG = struct_tagNET_DVR_CAMERA_DEHAZE_CFG
LPNET_DVR_CAMERA_DEHAZE_CFG = POINTER(struct_tagNET_DVR_CAMERA_DEHAZE_CFG)
tagNET_DVR_CAMERA_DEHAZE_CFG = struct_tagNET_DVR_CAMERA_DEHAZE_CFG
