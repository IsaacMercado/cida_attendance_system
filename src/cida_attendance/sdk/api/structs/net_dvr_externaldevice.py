from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_supplementlight import NET_DVR_SUPPLEMENTLIGHT


class struct_tagNET_DVR_EXTERNALDEVICE(Structure):
    pass

_S(struct_tagNET_DVR_EXTERNALDEVICE, [
    ('dwSize', DWORD),
    ('struSupplementLight', NET_DVR_SUPPLEMENTLIGHT),
    ('byRes', BYTE * 512),
])

NET_DVR_EXTERNALDEVICE = struct_tagNET_DVR_EXTERNALDEVICE
LPNET_DVR_EXTERNALDEVICE = POINTER(struct_tagNET_DVR_EXTERNALDEVICE)
tagNET_DVR_EXTERNALDEVICE = struct_tagNET_DVR_EXTERNALDEVICE
