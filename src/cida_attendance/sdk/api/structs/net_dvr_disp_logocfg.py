from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_DISP_LOGOCFG(Structure):
    pass

_S(struct_tagNET_DVR_DISP_LOGOCFG, [
    ('dwCorordinateX', DWORD),
    ('dwCorordinateY', DWORD),
    ('wPicWidth', WORD),
    ('wPicHeight', WORD),
    ('byRes1', BYTE * 4),
    ('byFlash', BYTE),
    ('byTranslucent', BYTE),
    ('byRes2', BYTE * 6),
    ('dwLogoSize', DWORD),
])

NET_DVR_DISP_LOGOCFG = struct_tagNET_DVR_DISP_LOGOCFG
LPNET_DVR_DISP_LOGOCFG = POINTER(struct_tagNET_DVR_DISP_LOGOCFG)
tagNET_DVR_DISP_LOGOCFG = struct_tagNET_DVR_DISP_LOGOCFG
