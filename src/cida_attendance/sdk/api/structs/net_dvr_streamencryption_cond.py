from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_STREAMENCRYPTION_COND(Structure):
    pass

_S(struct_tagNET_DVR_STREAMENCRYPTION_COND, [
    ('dwSize', DWORD),
    ('dwChan', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_STREAMENCRYPTION_COND = struct_tagNET_DVR_STREAMENCRYPTION_COND
LPNET_DVR_STREAMENCRYPTION_COND = POINTER(struct_tagNET_DVR_STREAMENCRYPTION_COND)
tagNET_DVR_STREAMENCRYPTION_COND = struct_tagNET_DVR_STREAMENCRYPTION_COND
