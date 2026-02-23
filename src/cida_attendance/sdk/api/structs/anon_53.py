from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_50 import NET_DVR_PPPCFG


class struct_anon_53(Structure):
    pass

_S(struct_anon_53, [
    ('dwSize', DWORD),
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('dwWorkMode', DWORD),
    ('struPPPConfig', NET_DVR_PPPCFG),
])

NET_DVR_RS232CFG = struct_anon_53
LPNET_DVR_RS232CFG = POINTER(struct_anon_53)
