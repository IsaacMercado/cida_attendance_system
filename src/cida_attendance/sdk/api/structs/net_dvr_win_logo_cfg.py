from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_WIN_LOGO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_WIN_LOGO_CFG, [
    ('dwSize', DWORD),
    ('dwLogoNo', DWORD),
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwCoordinateX', DWORD),
    ('dwCoordinateY', DWORD),
    ('byFlash', BYTE),
    ('byTranslucent', BYTE),
    ('byRes2', BYTE * 34),
])

NET_DVR_WIN_LOGO_CFG = struct_tagNET_DVR_WIN_LOGO_CFG
LPNET_DVR_WIN_LOGO_CFG = POINTER(struct_tagNET_DVR_WIN_LOGO_CFG)
tagNET_DVR_WIN_LOGO_CFG = struct_tagNET_DVR_WIN_LOGO_CFG
