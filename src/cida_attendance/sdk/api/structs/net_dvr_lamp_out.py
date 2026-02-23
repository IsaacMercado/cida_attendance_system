from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_lamp_status import NET_DVR_LAMP_STATUS


class struct__NET_DVR_LAMP_OUT(Structure):
    pass

_S(struct__NET_DVR_LAMP_OUT, [
    ('dwSize', DWORD),
    ('struLampInfo', NET_DVR_LAMP_STATUS * 2),
    ('byRes', BYTE * 256),
])

NET_DVR_LAMP_OUT = struct__NET_DVR_LAMP_OUT
LPNET_DVR_LAMP_OUT = POINTER(struct__NET_DVR_LAMP_OUT)
_NET_DVR_LAMP_OUT = struct__NET_DVR_LAMP_OUT
