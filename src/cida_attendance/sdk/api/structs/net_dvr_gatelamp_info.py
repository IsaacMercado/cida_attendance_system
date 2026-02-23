from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GATELAMP_INFO(Structure):
    pass

_S(struct_tagNET_DVR_GATELAMP_INFO, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byLaneNo', BYTE),
    ('byBrightlampCtrl', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_GATELAMP_INFO = struct_tagNET_DVR_GATELAMP_INFO
LPNET_DVR_GATELAMP_INFO = POINTER(struct_tagNET_DVR_GATELAMP_INFO)
tagNET_DVR_GATELAMP_INFO = struct_tagNET_DVR_GATELAMP_INFO
