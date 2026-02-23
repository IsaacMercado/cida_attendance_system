from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_308 import NET_DVR_INQUEST_PIP_PARAM


class struct_anon_309(Structure):
    pass

_S(struct_anon_309, [
    ('byBaseChan', BYTE),
    ('byBackChan', BYTE),
    ('byPIPMode', BYTE),
    ('byRes', BYTE),
    ('strPipPara', NET_DVR_INQUEST_PIP_PARAM * 3),
])

NET_DVR_INQUEST_PIP_STATUS = struct_anon_309
LPNET_DVR_INQUEST_PIP_STATUS = POINTER(struct_anon_309)
