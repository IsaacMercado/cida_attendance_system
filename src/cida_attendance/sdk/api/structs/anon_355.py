from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_355(Structure):
    pass

_S(struct_anon_355, [
    ('byVcaAlarmJsonType', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_MESSAGE_CALLBACK_PARAM_V51 = struct_anon_355
LPNET_DVR_MESSAGE_CALLBACK_PARAM_V51 = POINTER(struct_anon_355)
