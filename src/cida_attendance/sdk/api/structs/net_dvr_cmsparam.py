from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_CMSPARAM(Structure):
    pass

_S(struct_tagNET_DVR_CMSPARAM, [
    ('dwSize', DWORD),
    ('struCmsAddr', NET_DVR_IPADDR),
    ('wCmsPort', WORD),
    ('byRes1', BYTE * 2),
    ('sDeviceID', BYTE * 32),
    ('byPassword', BYTE * 16),
    ('struPicServerAddr', NET_DVR_IPADDR),
    ('wPicServerPort', WORD),
    ('wCmsUdpPort', WORD),
    ('byRes2', BYTE * 12),
])

NET_DVR_CMSPARAM = struct_tagNET_DVR_CMSPARAM
LPNET_DVR_CMSPARAM = POINTER(struct_tagNET_DVR_CMSPARAM)
tagNET_DVR_CMSPARAM = struct_tagNET_DVR_CMSPARAM
