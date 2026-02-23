from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subsysteminfo import NET_DVR_SUBSYSTEMINFO


class struct_tagNET_DVR_ALLSUBSYSTEMINFO(Structure):
    pass

_S(struct_tagNET_DVR_ALLSUBSYSTEMINFO, [
    ('dwSize', DWORD),
    ('struSubSystemInfo', NET_DVR_SUBSYSTEMINFO * 80),
    ('byRes', BYTE * 8),
])

NET_DVR_ALLSUBSYSTEMINFO = struct_tagNET_DVR_ALLSUBSYSTEMINFO
LPNET_DVR_ALLSUBSYSTEMINFO = POINTER(struct_tagNET_DVR_ALLSUBSYSTEMINFO)
tagNET_DVR_ALLSUBSYSTEMINFO = struct_tagNET_DVR_ALLSUBSYSTEMINFO
