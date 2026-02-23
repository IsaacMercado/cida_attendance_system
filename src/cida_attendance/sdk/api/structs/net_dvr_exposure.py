from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_EXPOSURE(Structure):
    pass

_S(struct_tagNET_DVR_EXPOSURE, [
    ('byExposureMode', BYTE),
    ('byAutoApertureLevel', BYTE),
    ('byRes', BYTE * 2),
    ('dwVideoExposureSet', DWORD),
    ('dwExposureUserSet', DWORD),
    ('dwRes', DWORD),
])

NET_DVR_EXPOSURE = struct_tagNET_DVR_EXPOSURE
LPNET_DVR_EXPOSURE = POINTER(struct_tagNET_DVR_EXPOSURE)
tagNET_DVR_EXPOSURE = struct_tagNET_DVR_EXPOSURE
