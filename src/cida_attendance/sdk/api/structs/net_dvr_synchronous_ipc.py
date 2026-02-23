from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SYNCHRONOUS_IPC(Structure):
    pass

_S(struct_tagNET_DVR_SYNCHRONOUS_IPC, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_SYNCHRONOUS_IPC = struct_tagNET_DVR_SYNCHRONOUS_IPC
LPNET_DVR_SYNCHRONOUS_IPC = POINTER(struct_tagNET_DVR_SYNCHRONOUS_IPC)
tagNET_DVR_SYNCHRONOUS_IPC = struct_tagNET_DVR_SYNCHRONOUS_IPC
