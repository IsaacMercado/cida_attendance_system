from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_structhead import NET_DVR_STRUCTHEAD


class struct_tagNET_DVR_RECORD_PACK(Structure):
    pass

_S(struct_tagNET_DVR_RECORD_PACK, [
    ('struStruceHead', NET_DVR_STRUCTHEAD),
    ('dwPackageInterval', DWORD),
    ('byRes', BYTE * 32),
])

NET_DVR_RECORD_PACK = struct_tagNET_DVR_RECORD_PACK
LPNET_DVR_RECORD_PACK = POINTER(struct_tagNET_DVR_RECORD_PACK)
tagNET_DVR_RECORD_PACK = struct_tagNET_DVR_RECORD_PACK
