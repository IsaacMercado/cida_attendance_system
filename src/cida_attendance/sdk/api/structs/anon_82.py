from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_72 import NET_DVR_IPDEVINFO
from .anon_73 import NET_DVR_IPCHANINFO
from .anon_78 import NET_DVR_IPALARMOUTINFO
from .anon_80 import NET_DVR_IPALARMININFO


class struct_anon_82(Structure):
    pass

_S(struct_anon_82, [
    ('struIPDevInfo', NET_DVR_IPDEVINFO * 32),
    ('byAnalogChanEnable', BYTE * 32),
    ('struIPChanInfo', NET_DVR_IPCHANINFO * 32),
    ('struIPAlarmInInfo', NET_DVR_IPALARMININFO * 128),
    ('struIPAlarmOutInfo', NET_DVR_IPALARMOUTINFO * 64),
])

NET_DVR_IPALARMINFO = struct_anon_82
LPNET_DVR_IPALARMINFO = POINTER(struct_anon_82)
