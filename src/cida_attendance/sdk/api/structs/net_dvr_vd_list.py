from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_vd_info import NET_DVR_VD_INFO


class struct_tagNET_DVR_VD_LIST(Structure):
    pass

_S(struct_tagNET_DVR_VD_LIST, [
    ('dwSize', DWORD),
    ('dwCount', DWORD),
    ('struVDInfo', NET_DVR_VD_INFO * 128),
])

NET_DVR_VD_LIST = struct_tagNET_DVR_VD_LIST
LPNET_DVR_VD_LIST = POINTER(struct_tagNET_DVR_VD_LIST)
tagNET_DVR_VD_LIST = struct_tagNET_DVR_VD_LIST
