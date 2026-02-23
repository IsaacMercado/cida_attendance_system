from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_external_lamp_ctrl_mode import NET_DVR_EXTERNAL_LAMP_CTRL_MODE
from .net_dvr_inlay_lamp_ctrl_mode import NET_DVR_INLAY_LAMP_CTRL_MODE
from .net_dvr_mixlamp_ctrl_mode import NET_DVR_MIXLAMP_CTRL_MODE
from .net_dvr_parklamp_ctrl_mode import NET_DVR_PARKLAMP_CTRL_MODE
from .net_dvr_singlelamp_ctrl_mode import NET_DVR_SINGLELAMP_CTRL_MODE


class union_tagNET_DVR_LAMP_CTRL_MODE_UNION(Union):
    pass

_S(union_tagNET_DVR_LAMP_CTRL_MODE_UNION, [
    ('uLen', BYTE * 288),
    ('struInlayLampCtrlMode', NET_DVR_INLAY_LAMP_CTRL_MODE),
    ('struExternalLampCtrlMode', NET_DVR_EXTERNAL_LAMP_CTRL_MODE),
    ('struParkLampCtrlMode', NET_DVR_PARKLAMP_CTRL_MODE * 4),
    ('struMixLampCtrlMode', NET_DVR_MIXLAMP_CTRL_MODE),
    ('struSingleExternalLampCtrlMode', NET_DVR_SINGLELAMP_CTRL_MODE),
])

NET_DVR_LAMP_CTRL_MODE_UNION = union_tagNET_DVR_LAMP_CTRL_MODE_UNION
LPNET_DVR_LAMP_CTRL_MODE_UNION = POINTER(union_tagNET_DVR_LAMP_CTRL_MODE_UNION)
tagNET_DVR_LAMP_CTRL_MODE_UNION = union_tagNET_DVR_LAMP_CTRL_MODE_UNION
