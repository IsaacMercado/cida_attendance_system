from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_MATRIX_UARTPARAM(Structure):
    pass

_S(struct_tagNET_MATRIX_UARTPARAM, [
    ('dwSize', DWORD),
    ('byPortName', BYTE * 32),
    ('wUserId', WORD),
    ('byPortType', BYTE),
    ('byFuncType', BYTE),
    ('byProtocolType', BYTE),
    ('byBaudRate', BYTE),
    ('byDataBits', BYTE),
    ('byStopBits', BYTE),
    ('byParity', BYTE),
    ('byFlowCtrl', BYTE),
    ('byRes', BYTE * 22),
])

NET_MATRIX_UARTPARAM = struct_tagNET_MATRIX_UARTPARAM
LPNET_MATRIX_UARTPARAM = POINTER(struct_tagNET_MATRIX_UARTPARAM)
tagNET_MATRIX_UARTPARAM = struct_tagNET_MATRIX_UARTPARAM
