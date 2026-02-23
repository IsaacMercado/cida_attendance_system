from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_control_info_union import NET_DVR_CONTROL_INFO_UNION


class struct_tagNET_DVR_RECORDING_CONTROL_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_RECORDING_CONTROL_CFG_, [
    ('dwSize', DWORD),
    ('wCmdType', WORD),
    ('byRes1', BYTE * 2),
    ('struControlInfo', NET_DVR_CONTROL_INFO_UNION),
    ('byRes', BYTE * 256),
])

NET_DVR_RECORDING_CONTROL_CFG = struct_tagNET_DVR_RECORDING_CONTROL_CFG_
LPNET_DVR_RECORDING_CONTROL_CFG = POINTER(struct_tagNET_DVR_RECORDING_CONTROL_CFG_)
tagNET_DVR_RECORDING_CONTROL_CFG_ = struct_tagNET_DVR_RECORDING_CONTROL_CFG_
