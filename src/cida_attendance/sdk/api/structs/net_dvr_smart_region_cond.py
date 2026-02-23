from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMART_REGION_COND(Structure):
    pass

_S(struct_tagNET_DVR_SMART_REGION_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwRegion', DWORD),
])

NET_DVR_SMART_REGION_COND = struct_tagNET_DVR_SMART_REGION_COND
LPNET_DVR_SMART_REGION_COND = POINTER(struct_tagNET_DVR_SMART_REGION_COND)
tagNET_DVR_SMART_REGION_COND = struct_tagNET_DVR_SMART_REGION_COND
