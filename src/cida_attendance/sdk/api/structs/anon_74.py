from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_72 import NET_DVR_IPDEVINFO
from .anon_73 import NET_DVR_IPCHANINFO


class struct_anon_74(Structure):
    pass

_S(struct_anon_74, [
    ('dwSize', DWORD),
    ('struIPDevInfo', NET_DVR_IPDEVINFO * 32),
    ('byAnalogChanEnable', BYTE * 32),
    ('struIPChanInfo', NET_DVR_IPCHANINFO * 32),
])

NET_DVR_IPPARACFG = struct_anon_74
LPNET_DVR_IPPARACFG = POINTER(struct_anon_74)
