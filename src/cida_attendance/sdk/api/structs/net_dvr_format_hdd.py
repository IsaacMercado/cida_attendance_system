from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_FORMAT_HDD(Structure):
    pass

_S(struct_tagNET_DVR_FORMAT_HDD, [
    ('dwSize', DWORD),
    ('dwDiskNo', DWORD),
    ('struLocateIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 16),
])

NET_DVR_FORMAT_HDD = struct_tagNET_DVR_FORMAT_HDD
LPNET_DVR_FORMAT_HDD = POINTER(struct_tagNET_DVR_FORMAT_HDD)
tagNET_DVR_FORMAT_HDD = struct_tagNET_DVR_FORMAT_HDD
