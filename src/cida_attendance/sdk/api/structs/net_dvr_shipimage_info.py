from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_SHIPIMAGE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_SHIPIMAGE_INFO, [
    ('dwShipImageLen', DWORD),
    ('pXmlBuf', String),
])

NET_DVR_SHIPIMAGE_INFO = struct_tagNET_DVR_SHIPIMAGE_INFO
LPNET_DVR_SHIPIMAGE_INFO = POINTER(struct_tagNET_DVR_SHIPIMAGE_INFO)
tagNET_DVR_SHIPIMAGE_INFO = struct_tagNET_DVR_SHIPIMAGE_INFO
