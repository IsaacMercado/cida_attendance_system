from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MOBILE_PLATE_RECOGCFG(Structure):
    pass

_S(struct_tagNET_DVR_MOBILE_PLATE_RECOGCFG, [
    ('dwSize', DWORD),
    ('byDefaultCHN', BYTE * 3),
    ('byTimeOsd', BYTE),
    ('byRecogResultOsd', BYTE),
    ('byRecogHint', BYTE),
    ('byRecogDir', BYTE),
    ('byRecogEnv', BYTE),
    ('byRecogPlateType', BYTE),
    ('byUploadPlate', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_MOBILE_PLATE_RECOGCFG = struct_tagNET_DVR_MOBILE_PLATE_RECOGCFG
LPNET_DVR_MOBILE_PLATE_RECOGCFG = POINTER(struct_tagNET_DVR_MOBILE_PLATE_RECOGCFG)
tagNET_DVR_MOBILE_PLATE_RECOGCFG = struct_tagNET_DVR_MOBILE_PLATE_RECOGCFG
