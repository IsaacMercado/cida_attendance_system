from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IPCHANINFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_IPCHANINFO_V40, [
    ('byEnable', BYTE),
    ('byRes1', BYTE),
    ('wIPID', WORD),
    ('dwChannel', DWORD),
    ('byTransProtocol', BYTE),
    ('byTransMode', BYTE),
    ('byFactoryType', BYTE),
    ('byRes', BYTE),
    ('strURL', BYTE * 240),
])

NET_DVR_IPCHANINFO_V40 = struct_tagNET_DVR_IPCHANINFO_V40
LPNET_DVR_IPCHANINFO_V40 = POINTER(struct_tagNET_DVR_IPCHANINFO_V40)
tagNET_DVR_IPCHANINFO_V40 = struct_tagNET_DVR_IPCHANINFO_V40
