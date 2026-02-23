from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_BV_CALIB_PIC(Structure):
    pass

_S(struct_tagNET_DVR_BV_CALIB_PIC, [
    ('dwSize', DWORD),
    ('dwPicID', DWORD),
    ('dwPicLen1', DWORD),
    ('dwPicLen2', DWORD),
    ('pPicBuffer1', String),
    ('pPicBuffer2', String),
    ('byRes', BYTE * 600),
])

NET_DVR_BV_CALIB_PIC = struct_tagNET_DVR_BV_CALIB_PIC
LPNET_DVR_BV_CALIB_PIC = POINTER(struct_tagNET_DVR_BV_CALIB_PIC)
tagNET_DVR_BV_CALIB_PIC = struct_tagNET_DVR_BV_CALIB_PIC
