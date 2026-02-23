from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_IDENTIFICATION_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_IDENTIFICATION_PARAM, [
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byRes1', BYTE * 4),
])

NET_DVR_IDENTIFICATION_PARAM = struct_tagNET_DVR_IDENTIFICATION_PARAM
LPNET_DVR_IDENTIFICATION_PARAM = POINTER(struct_tagNET_DVR_IDENTIFICATION_PARAM)
tagNET_DVR_IDENTIFICATION_PARAM = struct_tagNET_DVR_IDENTIFICATION_PARAM
