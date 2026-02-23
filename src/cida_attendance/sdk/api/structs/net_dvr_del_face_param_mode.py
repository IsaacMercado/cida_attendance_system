from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_face_param_bycard import NET_DVR_FACE_PARAM_BYCARD
from .net_dvr_face_param_byreader import NET_DVR_FACE_PARAM_BYREADER


class union_tagNET_DVR_DEL_FACE_PARAM_MODE(Union):
    pass

_S(union_tagNET_DVR_DEL_FACE_PARAM_MODE, [
    ('uLen', BYTE * 588),
    ('struByCard', NET_DVR_FACE_PARAM_BYCARD),
    ('struByReader', NET_DVR_FACE_PARAM_BYREADER),
])

NET_DVR_DEL_FACE_PARAM_MODE = union_tagNET_DVR_DEL_FACE_PARAM_MODE
LPNET_DVR_DEL_FACE_PARAM_MODE = POINTER(union_tagNET_DVR_DEL_FACE_PARAM_MODE)
tagNET_DVR_DEL_FACE_PARAM_MODE = union_tagNET_DVR_DEL_FACE_PARAM_MODE
