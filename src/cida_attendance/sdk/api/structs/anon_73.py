from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_73(Structure):
    pass

_S(struct_anon_73, [
    ('byEnable', BYTE),
    ('byIPID', BYTE),
    ('byChannel', BYTE),
    ('byIPIDHigh', BYTE),
    ('byTransProtocol', BYTE),
    ('byGetStream', BYTE),
    ('byres', BYTE * 30),
])

NET_DVR_IPCHANINFO = struct_anon_73
LPNET_DVR_IPCHANINFO = POINTER(struct_anon_73)
