from ctypes import Union

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_add_param import NET_DVR_ADD_PARAM
from .net_dvr_del_param import NET_DVR_DEL_PARAM


class union_tagNET_DVR_NPO_PARAM_UNION(Union):
    pass

_S(union_tagNET_DVR_NPO_PARAM_UNION, [
    ('struAddParam', NET_DVR_ADD_PARAM),
    ('struDelParam', NET_DVR_DEL_PARAM),
])

NET_DVR_NPO_PARAM_UNION = union_tagNET_DVR_NPO_PARAM_UNION
LPNET_DVR_NPO_PARAM_UNION = POINTER(union_tagNET_DVR_NPO_PARAM_UNION)
tagNET_DVR_NPO_PARAM_UNION = union_tagNET_DVR_NPO_PARAM_UNION
