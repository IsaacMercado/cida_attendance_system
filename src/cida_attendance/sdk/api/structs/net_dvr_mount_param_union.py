from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_identification_param import NET_DVR_IDENTIFICATION_PARAM


class union_tagNET_DVR_MOUNT_PARAM_UNION(Union):
    pass

_S(union_tagNET_DVR_MOUNT_PARAM_UNION, [
    ('uLen', BYTE * 52),
    ('struIdentificationParam', NET_DVR_IDENTIFICATION_PARAM),
])

NET_DVR_MOUNT_PARAM_UNION = union_tagNET_DVR_MOUNT_PARAM_UNION
LPNET_DVR_MOUNT_PARAM_UNION = POINTER(union_tagNET_DVR_MOUNT_PARAM_UNION)
tagNET_DVR_MOUNT_PARAM_UNION = union_tagNET_DVR_MOUNT_PARAM_UNION
