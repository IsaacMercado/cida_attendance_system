from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_REDUNDANT_DEVICE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_REDUNDANT_DEVICE_INFO, [
    ('struIP', NET_DVR_IPADDR),
    ('byWorkStatus', BYTE),
    ('byBackupStatus', BYTE),
    ('wBackupPort', WORD),
])

NET_DVR_REDUNDANT_DEVICE_INFO = struct_tagNET_DVR_REDUNDANT_DEVICE_INFO
LPNET_DVR_REDUNDANT_DEVICE_INFO = POINTER(struct_tagNET_DVR_REDUNDANT_DEVICE_INFO)
tagNET_DVR_REDUNDANT_DEVICE_INFO = struct_tagNET_DVR_REDUNDANT_DEVICE_INFO
