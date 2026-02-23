from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_anon_298(Structure):
    pass

_S(struct_anon_298, [
    ('byItemOrder', BYTE * 15),
    ('byDelimiter', BYTE),
    ('byPicNamePrefix', BYTE * 32),
])

NET_DVR_PICTURE_NAME_EX = struct_anon_298
LPNET_DVR_PICTURE_NAME_EX = POINTER(struct_anon_298)
