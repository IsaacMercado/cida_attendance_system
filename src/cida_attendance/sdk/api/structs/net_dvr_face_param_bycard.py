from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACE_PARAM_BYCARD(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PARAM_BYCARD, [
    ('byCardNo', BYTE * 32),
    ('byEnableCardReader', BYTE * 512),
    ('byFaceID', BYTE * 2),
    ('byRes1', BYTE * 42),
])

NET_DVR_FACE_PARAM_BYCARD = struct_tagNET_DVR_FACE_PARAM_BYCARD
LPNET_DVR_FACE_PARAM_BYCARD = POINTER(struct_tagNET_DVR_FACE_PARAM_BYCARD)
tagNET_DVR_FACE_PARAM_BYCARD = struct_tagNET_DVR_FACE_PARAM_BYCARD
