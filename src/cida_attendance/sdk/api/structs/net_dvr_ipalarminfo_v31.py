from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_73 import NET_DVR_IPCHANINFO
from .anon_78 import NET_DVR_IPALARMOUTINFO
from .anon_80 import NET_DVR_IPALARMININFO
from .net_dvr_ipdevinfo_v31 import NET_DVR_IPDEVINFO_V31


class struct_tagNET_DVR_IPALARMINFO_V31(Structure):
    pass

_S(struct_tagNET_DVR_IPALARMINFO_V31, [
    ('struIPDevInfo', NET_DVR_IPDEVINFO_V31 * 32),
    ('byAnalogChanEnable', BYTE * 32),
    ('struIPChanInfo', NET_DVR_IPCHANINFO * 32),
    ('struIPAlarmInInfo', NET_DVR_IPALARMININFO * 128),
    ('struIPAlarmOutInfo', NET_DVR_IPALARMOUTINFO * 64),
])

NET_DVR_IPALARMINFO_V31 = struct_tagNET_DVR_IPALARMINFO_V31
LPNET_DVR_IPALARMINFO_V31 = POINTER(struct_tagNET_DVR_IPALARMINFO_V31)
tagNET_DVR_IPALARMINFO_V31 = struct_tagNET_DVR_IPALARMINFO_V31
