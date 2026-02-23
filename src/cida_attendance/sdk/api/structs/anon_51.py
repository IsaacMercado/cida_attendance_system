from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD


class struct_anon_51(Structure):
    pass

_S(struct_anon_51, [
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('dwWorkMode', DWORD),
])

NET_DVR_SINGLE_RS232 = struct_anon_51
