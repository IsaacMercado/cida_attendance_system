from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_dvr_param import NET_DVR_DVR_PARAM
from .net_dvr_lun_param import NET_DVR_LUN_PARAM
from .net_dvr_operate_vd_param import NET_DVR_OPERATE_VD_PARAM


class union_tagNET_DVR_VD_UNION(Union):
    pass

_S(union_tagNET_DVR_VD_UNION, [
    ('byUnionLen', BYTE * 256),
    ('struHikVDParam', NET_DVR_OPERATE_VD_PARAM),
    ('struLunParam', NET_DVR_LUN_PARAM),
    ('struDvrParam', NET_DVR_DVR_PARAM),
])

NET_DVR_VD_UNION = union_tagNET_DVR_VD_UNION
LPNET_DVR_VD_UNION = POINTER(union_tagNET_DVR_VD_UNION)
tagNET_DVR_VD_UNION = union_tagNET_DVR_VD_UNION
