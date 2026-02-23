from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_TRANSFER_CAP(Structure):
    pass

_S(struct_tagNET_DVR_TRANSFER_CAP, [
    ('byAbility', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_TRANSFER_CAP = struct_tagNET_DVR_TRANSFER_CAP
LPNET_DVR_TRANSFER_CAP = POINTER(struct_tagNET_DVR_TRANSFER_CAP)
tagNET_DVR_TRANSFER_CAP = struct_tagNET_DVR_TRANSFER_CAP
