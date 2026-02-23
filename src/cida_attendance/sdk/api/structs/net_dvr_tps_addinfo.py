from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_llpos_param import NET_DVR_LLPOS_PARAM
from .net_dvr_stop_line_param import NET_DVR_STOP_LINE_PARAM
from .net_dvr_turn_direction_param import NET_DVR_TURN_DIRECTION_PARAM


class struct_tagNET_DVR_TPS_ADDINFO(Structure):
    pass

_S(struct_tagNET_DVR_TPS_ADDINFO, [
    ('struFirstLLPos', NET_DVR_LLPOS_PARAM),
    ('struLastLLPos', NET_DVR_LLPOS_PARAM),
    ('sLicense', c_char * 16),
    ('struTurnDirection', NET_DVR_TURN_DIRECTION_PARAM),
    ('struStopLine', NET_DVR_STOP_LINE_PARAM),
    ('byRes', BYTE * 884),
])

NET_DVR_TPS_ADDINFO = struct_tagNET_DVR_TPS_ADDINFO
LPNET_DVR_TPS_ADDINFO = POINTER(struct_tagNET_DVR_TPS_ADDINFO)
tagNET_DVR_TPS_ADDINFO = struct_tagNET_DVR_TPS_ADDINFO
