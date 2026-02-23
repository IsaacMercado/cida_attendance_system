from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_advance_cond_union import NET_DVR_ADVANCE_COND_UNION
from .net_dvr_ptzpos_info import NET_DVR_PTZPOS_INFO
from .net_vca_intrusion import NET_VCA_INTRUSION


class struct_tagNET_DVR_INTRUSION_SEARCHCOND(Structure):
    pass

_S(struct_tagNET_DVR_INTRUSION_SEARCHCOND, [
    ('struVcaIntrusion', NET_VCA_INTRUSION * 8),
    ('dwPreTime', DWORD),
    ('dwDelayTime', DWORD),
    ('struPTZPosInfo', NET_DVR_PTZPOS_INFO),
    ('byAdvanceType', BYTE),
    ('byRes1', BYTE * 3),
    ('uAdvanceCond', NET_DVR_ADVANCE_COND_UNION),
    ('byRes', BYTE * 5348),
])

NET_DVR_INTRUSION_SEARCHCOND = struct_tagNET_DVR_INTRUSION_SEARCHCOND
LPNET_DVR_INTRUSION_SEARCHCOND = POINTER(struct_tagNET_DVR_INTRUSION_SEARCHCOND)
tagNET_DVR_INTRUSION_SEARCHCOND = struct_tagNET_DVR_INTRUSION_SEARCHCOND
