from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_ipdevinfo_v31 import NET_DVR_IPDEVINFO_V31
from .net_dvr_stream_mode import NET_DVR_STREAM_MODE


class struct_tagNET_DVR_IPPARACFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_IPPARACFG_V40, [
    ('dwSize', DWORD),
    ('dwGroupNum', DWORD),
    ('dwAChanNum', DWORD),
    ('dwDChanNum', DWORD),
    ('dwStartDChan', DWORD),
    ('byAnalogChanEnable', BYTE * int((32 + 32))),
    ('struIPDevInfo', NET_DVR_IPDEVINFO_V31 * 64),
    ('struStreamMode', NET_DVR_STREAM_MODE * int((32 + 32))),
    ('byRes2', BYTE * 20),
])

NET_DVR_IPPARACFG_V40 = struct_tagNET_DVR_IPPARACFG_V40
LPNET_DVR_IPPARACFG_V40 = POINTER(struct_tagNET_DVR_IPPARACFG_V40)
tagNET_DVR_IPPARACFG_V40 = struct_tagNET_DVR_IPPARACFG_V40
