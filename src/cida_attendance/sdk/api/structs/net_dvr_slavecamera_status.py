from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_slavecamera_param import NET_DVR_SLAVECAMERA_PARAM


class struct_tagNET_DVR_SLAVECAMERA_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_SLAVECAMERA_STATUS, [
    ('dwSize', DWORD),
    ('struSlaveCamera', NET_DVR_SLAVECAMERA_PARAM * 8),
    ('byRes', BYTE * 64),
])

NET_DVR_SLAVECAMERA_STATUS = struct_tagNET_DVR_SLAVECAMERA_STATUS
LPNET_DVR_SLAVECAMERA_STATUS = POINTER(struct_tagNET_DVR_SLAVECAMERA_STATUS)
tagNET_DVR_SLAVECAMERA_STATUS = struct_tagNET_DVR_SLAVECAMERA_STATUS
