from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subsysteminfo_v40 import NET_DVR_SUBSYSTEMINFO_V40


class struct_tagNET_DVR_ALLSUBSYSTEMINFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_ALLSUBSYSTEMINFO_V40, [
    ('dwSize', DWORD),
    ('struSubSystemInfo', NET_DVR_SUBSYSTEMINFO_V40 * 120),
    ('byRes', BYTE * 8),
])

NET_DVR_ALLSUBSYSTEMINFO_V40 = struct_tagNET_DVR_ALLSUBSYSTEMINFO_V40
LPNET_DVR_ALLSUBSYSTEMINFO_V40 = POINTER(struct_tagNET_DVR_ALLSUBSYSTEMINFO_V40)
tagNET_DVR_ALLSUBSYSTEMINFO_V40 = struct_tagNET_DVR_ALLSUBSYSTEMINFO_V40
