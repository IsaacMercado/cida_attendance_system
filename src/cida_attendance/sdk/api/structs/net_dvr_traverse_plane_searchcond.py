from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_advance_cond_union import NET_DVR_ADVANCE_COND_UNION
from .net_dvr_ptzpos_info import NET_DVR_PTZPOS_INFO
from .net_vca_traverse_plane import NET_VCA_TRAVERSE_PLANE


class struct_tagNET_DVR_TRAVERSE_PLANE_SEARCHCOND(Structure):
    pass

_S(struct_tagNET_DVR_TRAVERSE_PLANE_SEARCHCOND, [
    ('struVcaTraversePlane', NET_VCA_TRAVERSE_PLANE * 8),
    ('dwPreTime', DWORD),
    ('dwDelayTime', DWORD),
    ('struPTZPosInfo', NET_DVR_PTZPOS_INFO),
    ('byAdvanceType', BYTE),
    ('byRes1', BYTE * 3),
    ('uAdvanceCond', NET_DVR_ADVANCE_COND_UNION),
    ('byRes', BYTE * 5604),
])

NET_DVR_TRAVERSE_PLANE_SEARCHCOND = struct_tagNET_DVR_TRAVERSE_PLANE_SEARCHCOND
LPNET_DVR_TRAVERSE_PLANE_SEARCHCOND = POINTER(struct_tagNET_DVR_TRAVERSE_PLANE_SEARCHCOND)
tagNET_DVR_TRAVERSE_PLANE_SEARCHCOND = struct_tagNET_DVR_TRAVERSE_PLANE_SEARCHCOND
