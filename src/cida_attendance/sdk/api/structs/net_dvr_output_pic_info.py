from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OUTPUT_PIC_INFO(Structure):
    pass

_S(struct_tagNET_DVR_OUTPUT_PIC_INFO, [
    ('dwSize', DWORD),
    ('sPicName', BYTE * 32),
    ('byUsed', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_OUTPUT_PIC_INFO = struct_tagNET_DVR_OUTPUT_PIC_INFO
LPNET_DVR_OUTPUT_PIC_INFO = POINTER(struct_tagNET_DVR_OUTPUT_PIC_INFO)
tagNET_DVR_OUTPUT_PIC_INFO = struct_tagNET_DVR_OUTPUT_PIC_INFO
