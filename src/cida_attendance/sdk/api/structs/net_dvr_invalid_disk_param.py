from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_structhead import NET_DVR_STRUCTHEAD


class struct_tagNET_DVR_INVALID_DISK_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_INVALID_DISK_PARAM, [
    ('struStructHead', NET_DVR_STRUCTHEAD),
    ('dwDiskNo', DWORD),
    ('byDelAll', BYTE),
    ('byres', BYTE * 31),
])

NET_DVR_INVALID_DISK_PARAM = struct_tagNET_DVR_INVALID_DISK_PARAM
LPNET_DVR_INVALID_DISK_PARAM = POINTER(struct_tagNET_DVR_INVALID_DISK_PARAM)
tagNET_DVR_INVALID_DISK_PARAM = struct_tagNET_DVR_INVALID_DISK_PARAM
