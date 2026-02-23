from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_parkspace_info import NET_DVR_PARKSPACE_INFO


class struct_tagNET_DVR_PARKSPACE_ATTRIBUTE(Structure):
    pass

_S(struct_tagNET_DVR_PARKSPACE_ATTRIBUTE, [
    ('dwSize', DWORD),
    ('struParkSpaceInfo', NET_DVR_PARKSPACE_INFO * 4),
    ('byRes', BYTE * 64),
])

NET_DVR_PARKSPACE_ATTRIBUTE = struct_tagNET_DVR_PARKSPACE_ATTRIBUTE
LPNET_DVR_PARKSPACE_ATTRIBUTE = POINTER(struct_tagNET_DVR_PARKSPACE_ATTRIBUTE)
tagNET_DVR_PARKSPACE_ATTRIBUTE = struct_tagNET_DVR_PARKSPACE_ATTRIBUTE
