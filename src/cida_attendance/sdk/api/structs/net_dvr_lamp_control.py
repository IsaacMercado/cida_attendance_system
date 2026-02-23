from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct__NET_DVR_LAMP_CONTROL(Structure):
    pass

_S(struct__NET_DVR_LAMP_CONTROL, [
    ('dwSize', DWORD),
    ('byLampNo', BYTE),
    ('byLampStateNo', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_LAMP_CONTROL = struct__NET_DVR_LAMP_CONTROL
LPNET_DVR_LAMP_CONTROL = POINTER(struct__NET_DVR_LAMP_CONTROL)
_NET_DVR_LAMP_CONTROL = struct__NET_DVR_LAMP_CONTROL
