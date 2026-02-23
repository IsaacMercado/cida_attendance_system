from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SINGLE_HDGROUP_V40(Structure):
    pass

_S(struct_tagNET_DVR_SINGLE_HDGROUP_V40, [
    ('dwHDGroupNo', DWORD),
    ('dwRelRecordChan', DWORD * 512),
    ('byRes', BYTE * 64),
])

NET_DVR_SINGLE_HDGROUP_V40 = struct_tagNET_DVR_SINGLE_HDGROUP_V40
LPNET_DVR_SINGLE_HDGROUP_V40 = POINTER(struct_tagNET_DVR_SINGLE_HDGROUP_V40)
tagNET_DVR_SINGLE_HDGROUP_V40 = struct_tagNET_DVR_SINGLE_HDGROUP_V40
