from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_control_delay_cfg import NET_DVR_CONTROL_DELAY_CFG
from .net_dvr_control_start_cfg import NET_DVR_CONTROL_START_CFG


class union_tagNET_DVR_CONTROL_INFO_UNION(Union):
    pass

_S(union_tagNET_DVR_CONTROL_INFO_UNION, [
    ('byLen', BYTE * 132),
    ('struStartCfg', NET_DVR_CONTROL_START_CFG),
    ('struDelayCfg', NET_DVR_CONTROL_DELAY_CFG),
])

NET_DVR_CONTROL_INFO_UNION = union_tagNET_DVR_CONTROL_INFO_UNION
LPNET_DVR_CONTROL_INFO_UNION = POINTER(union_tagNET_DVR_CONTROL_INFO_UNION)
tagNET_DVR_CONTROL_INFO_UNION = union_tagNET_DVR_CONTROL_INFO_UNION
