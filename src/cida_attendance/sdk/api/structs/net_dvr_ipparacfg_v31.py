from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_73 import NET_DVR_IPCHANINFO
from .net_dvr_ipdevinfo_v31 import NET_DVR_IPDEVINFO_V31


class struct_tagNET_DVR_IPPARACFG_V31(Structure):
    pass

_S(struct_tagNET_DVR_IPPARACFG_V31, [
    ('dwSize', DWORD),
    ('struIPDevInfo', NET_DVR_IPDEVINFO_V31 * 32),
    ('byAnalogChanEnable', BYTE * 32),
    ('struIPChanInfo', NET_DVR_IPCHANINFO * 32),
])

NET_DVR_IPPARACFG_V31 = struct_tagNET_DVR_IPPARACFG_V31
LPNET_DVR_IPPARACFG_V31 = POINTER(struct_tagNET_DVR_IPPARACFG_V31)
tagNET_DVR_IPPARACFG_V31 = struct_tagNET_DVR_IPPARACFG_V31
