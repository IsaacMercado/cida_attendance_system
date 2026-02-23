from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_plate_info import NET_DVR_PLATE_INFO
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_PLATERECO_RESULE(Structure):
    pass

_S(struct_tagNET_DVR_PLATERECO_RESULE, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('dwPicDataLen', DWORD),
    ('dwRes', DWORD * 4),
    ('pImage', POINTER(BYTE)),
])

NET_DVR_PLATERECO_RESULE = struct_tagNET_DVR_PLATERECO_RESULE
LPNET_DVR_PLATERECO_RESULE = POINTER(struct_tagNET_DVR_PLATERECO_RESULE)
tagNET_DVR_PLATERECO_RESULE = struct_tagNET_DVR_PLATERECO_RESULE
