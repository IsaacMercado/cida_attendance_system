from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_PIP_PARAM_V40(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_PIP_PARAM_V40, [
    ('byPipChan', BYTE),
    ('byRes1', BYTE * 3),
    ('wTopLeftX', WORD),
    ('wTopLeftY', WORD),
    ('wHeight', WORD),
    ('wWidth', WORD),
    ('byRes2', BYTE * 32),
])

NET_DVR_INQUEST_PIP_PARAM_V40 = struct_tagNET_DVR_INQUEST_PIP_PARAM_V40
LPNET_DVR_INQUEST_PIP_PARAM_V40 = POINTER(struct_tagNET_DVR_INQUEST_PIP_PARAM_V40)
tagNET_DVR_INQUEST_PIP_PARAM_V40 = struct_tagNET_DVR_INQUEST_PIP_PARAM_V40
