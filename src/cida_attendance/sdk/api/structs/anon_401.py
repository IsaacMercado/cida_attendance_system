from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_401(Structure):
    pass

_S(struct_anon_401, [
    ('byOutPutState1', BYTE),
    ('byOutPutState2', BYTE),
    ('byOutPutState3', BYTE),
    ('byOutPutState4', BYTE),
    ('byOutPutState5', BYTE),
    ('byOutPutState6', BYTE),
    ('Res', BYTE * 506),
])

NET_DVR_GENERATE_OUTPUT_STATE = struct_anon_401
LPNET_DVR_GENERATE_OUTPUT_STATE = POINTER(struct_anon_401)
