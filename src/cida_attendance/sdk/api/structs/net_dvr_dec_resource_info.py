from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_DEC_RESOURCE_INFO(Structure):
    pass

_S(struct_tagNET_DVR_DEC_RESOURCE_INFO, [
    ('dwSize', DWORD),
    ('dwSlotNum', DWORD),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes1', BYTE * 2),
    ('dwDecChan', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRes2', BYTE * 32),
])

NET_DVR_DEC_RESOURCE_INFO = struct_tagNET_DVR_DEC_RESOURCE_INFO
LPNET_DVR_DEC_RESOURCE_INFO = POINTER(struct_tagNET_DVR_DEC_RESOURCE_INFO)
tagNET_DVR_DEC_RESOURCE_INFO = struct_tagNET_DVR_DEC_RESOURCE_INFO
