from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_MB_DOWNLOADSVRPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_DOWNLOADSVRPARA, [
    ('dwSize', DWORD),
    ('struDownloadSvrIp', NET_DVR_IPADDR),
    ('byRes', BYTE * 64),
])

NET_DVR_MB_DOWNLOADSVRPARA = struct_tagNET_DVR_MB_DOWNLOADSVRPARA
LPNET_DVR_MB_DOWNLOADSVRPARA = POINTER(struct_tagNET_DVR_MB_DOWNLOADSVRPARA)
tagNET_DVR_MB_DOWNLOADSVRPARA = struct_tagNET_DVR_MB_DOWNLOADSVRPARA
