from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_behavior_info import NET_DVR_BEHAVIOR_INFO
from .net_dvr_face_sub_pic_info import NET_DVR_FACE_SUB_PIC_INFO
from .net_dvr_plate_info import NET_DVR_PLATE_INFO


class union_tagNET_DVR_PIC_FEATURE_UNION(Union):
    pass

_S(union_tagNET_DVR_PIC_FEATURE_UNION, [
    ('byLen', BYTE * 256),
    ('struPlateInfo', NET_DVR_PLATE_INFO),
    ('struFaceSubInfo', NET_DVR_FACE_SUB_PIC_INFO),
    ('struBehavior', NET_DVR_BEHAVIOR_INFO),
])

NET_DVR_PIC_FEATURE_UNION = union_tagNET_DVR_PIC_FEATURE_UNION
LPNET_DVR_PIC_FEATURE_UNION = POINTER(union_tagNET_DVR_PIC_FEATURE_UNION)
tagNET_DVR_PIC_FEATURE_UNION = union_tagNET_DVR_PIC_FEATURE_UNION
