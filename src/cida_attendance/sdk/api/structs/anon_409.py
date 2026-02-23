from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_409(Structure):
    pass

_S(struct_anon_409, [
    ('dwSize', DWORD),
    ('byOutPutState1', BYTE),
    ('byOutPutState2', BYTE),
    ('byOutPutState3', BYTE),
    ('byOutPutState4', BYTE),
    ('byOutPutState5', BYTE),
    ('byOutPutState6', BYTE),
    ('byOperateType', BYTE),
    ('Res', BYTE * 65),
])

NET_DVR_GENERATE_OUTPUT_CTRL = struct_anon_409
LPNET_DVR_GENERATE_OUTPUT_CTRL = POINTER(struct_anon_409)
