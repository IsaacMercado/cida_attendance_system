from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_PREVIEWPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PREVIEWPARAM, [
    ('byTransProtol', BYTE),
    ('byTransMode', BYTE),
    ('struCuIp', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('wUdpPort', WORD),
    ('bySupportQos', BYTE),
    ('byNatRequest', BYTE),
    ('byPreviewType', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_PREVIEWPARAM = struct_tagNET_DVR_PREVIEWPARAM
LPNET_DVR_PREVIEWPARAM = POINTER(struct_tagNET_DVR_PREVIEWPARAM)
tagNET_DVR_PREVIEWPARAM = struct_tagNET_DVR_PREVIEWPARAM
