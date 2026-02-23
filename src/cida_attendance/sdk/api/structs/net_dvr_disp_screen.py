from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISP_SCREEN(Structure):
    pass

_S(struct_tagNET_DVR_DISP_SCREEN, [
    ('dwSize', DWORD),
    ('wScreenID', WORD),
    ('byWallNo', BYTE),
    ('byRes1', BYTE),
    ('dwDeviceIndex', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_DISP_SCREEN = struct_tagNET_DVR_DISP_SCREEN
LPNET_DVR_DISP_SCREEN = POINTER(struct_tagNET_DVR_DISP_SCREEN)
tagNET_DVR_DISP_SCREEN = struct_tagNET_DVR_DISP_SCREEN
