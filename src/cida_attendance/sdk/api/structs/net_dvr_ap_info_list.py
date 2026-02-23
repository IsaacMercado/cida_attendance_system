from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ap_info import NET_DVR_AP_INFO


class struct_tagNET_DVR_AP_INFO_LIST(Structure):
    pass

_S(struct_tagNET_DVR_AP_INFO_LIST, [
    ('dwSize', DWORD),
    ('dwCount', DWORD),
    ('struApInfo', NET_DVR_AP_INFO * 20),
])

NET_DVR_AP_INFO_LIST = struct_tagNET_DVR_AP_INFO_LIST
LPNET_DVR_AP_INFO_LIST = POINTER(struct_tagNET_DVR_AP_INFO_LIST)
tagNET_DVR_AP_INFO_LIST = struct_tagNET_DVR_AP_INFO_LIST
