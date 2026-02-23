from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_npo_dev_info_union import NET_DVR_NPO_DEV_INFO_UNION


class struct_tagNET_DVR_N_PLUS_ONE_DEVICE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_N_PLUS_ONE_DEVICE_INFO, [
    ('dwSize', DWORD),
    ('unionDevInfo', NET_DVR_NPO_DEV_INFO_UNION),
    ('byType', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_N_PLUS_ONE_DEVICE_INFO = struct_tagNET_DVR_N_PLUS_ONE_DEVICE_INFO
LPNET_DVR_N_PLUS_ONE_DEVICE_INFO = POINTER(struct_tagNET_DVR_N_PLUS_ONE_DEVICE_INFO)
tagNET_DVR_N_PLUS_ONE_DEVICE_INFO = struct_tagNET_DVR_N_PLUS_ONE_DEVICE_INFO
