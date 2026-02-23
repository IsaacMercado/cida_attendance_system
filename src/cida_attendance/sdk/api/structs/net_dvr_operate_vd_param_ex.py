from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_vd_union import NET_DVR_VD_UNION


class struct_tagNET_DVR_OPERATE_VD_PARAM_EX(Structure):
    pass

_S(struct_tagNET_DVR_OPERATE_VD_PARAM_EX, [
    ('byVDType', BYTE),
    ('byRes1', BYTE * 3),
    ('uVDParam', NET_DVR_VD_UNION),
    ('byRes2', BYTE * 32),
])

NET_DVR_OPERATE_VD_PARAM_EX = struct_tagNET_DVR_OPERATE_VD_PARAM_EX
LPNET_DVR_OPERATE_VD_PARAM_EX = POINTER(struct_tagNET_DVR_OPERATE_VD_PARAM_EX)
tagNET_DVR_OPERATE_VD_PARAM_EX = struct_tagNET_DVR_OPERATE_VD_PARAM_EX
