from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_firmwarecode import NET_DVR_FIRMWARECODE


class struct_tagNET_DVR_FIRMWARECODE_LIST(Structure):
    pass

_S(struct_tagNET_DVR_FIRMWARECODE_LIST, [
    ('dwSize', DWORD),
    ('dwValidCodeNum', DWORD),
    ('struCode', NET_DVR_FIRMWARECODE * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_FIRMWARECODE_LIST = struct_tagNET_DVR_FIRMWARECODE_LIST
LPNET_DVR_FIRMWARECODE_LIST = POINTER(struct_tagNET_DVR_FIRMWARECODE_LIST)
tagNET_DVR_FIRMWARECODE_LIST = struct_tagNET_DVR_FIRMWARECODE_LIST
