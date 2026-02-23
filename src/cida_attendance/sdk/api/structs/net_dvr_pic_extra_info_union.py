from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_face_extra_info import NET_DVR_FACE_EXTRA_INFO


class union_tagNET_DVR_PIC_EXTRA_INFO_UNION(Union):
    pass

_S(union_tagNET_DVR_PIC_EXTRA_INFO_UNION, [
    ('byUnionLen', BYTE * 544),
    ('struFaceExtraInfo', NET_DVR_FACE_EXTRA_INFO),
])

NET_DVR_PIC_EXTRA_INFO_UNION = union_tagNET_DVR_PIC_EXTRA_INFO_UNION
LPNET_DVR_PIC_EXTRA_INFO_UNION = POINTER(union_tagNET_DVR_PIC_EXTRA_INFO_UNION)
tagNET_DVR_PIC_EXTRA_INFO_UNION = union_tagNET_DVR_PIC_EXTRA_INFO_UNION
