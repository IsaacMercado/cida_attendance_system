from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_GAMMACORRECT(Structure):
    pass

_S(struct_tagNET_DVR_GAMMACORRECT, [
    ('byGammaCorrectionEnabled', BYTE),
    ('byGammaCorrectionLevel', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_GAMMACORRECT = struct_tagNET_DVR_GAMMACORRECT
LPNET_DVR_GAMMACORRECT = POINTER(struct_tagNET_DVR_GAMMACORRECT)
tagNET_DVR_GAMMACORRECT = struct_tagNET_DVR_GAMMACORRECT
