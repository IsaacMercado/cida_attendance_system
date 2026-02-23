from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ipalarmoutinfo_v40 import NET_DVR_IPALARMOUTINFO_V40


class struct_tagNET_DVR_IPALARMOUTCFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_IPALARMOUTCFG_V40, [
    ('dwSize', DWORD),
    ('dwCurIPAlarmOutNum', DWORD),
    ('struIPAlarmOutInfo', NET_DVR_IPALARMOUTINFO_V40 * 4096),
    ('byRes', BYTE * 256),
])

NET_DVR_IPALARMOUTCFG_V40 = struct_tagNET_DVR_IPALARMOUTCFG_V40
LPNET_DVR_IPALARMOUTCFG_V40 = POINTER(struct_tagNET_DVR_IPALARMOUTCFG_V40)
tagNET_DVR_IPALARMOUTCFG_V40 = struct_tagNET_DVR_IPALARMOUTCFG_V40
