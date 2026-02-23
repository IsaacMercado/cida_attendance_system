from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_polygon import NET_VCA_POLYGON


class struct__NET_VCA_RUNNING_(Structure):
    pass

_S(struct__NET_VCA_RUNNING_, [
    ('struRegion', NET_VCA_POLYGON),
    ('dwSpeed', DWORD),
    ('byRes', BYTE * 4),
])

NET_VCA_RUNNING = struct__NET_VCA_RUNNING_
LPNET_VCA_RUNNING = POINTER(struct__NET_VCA_RUNNING_)
_NET_VCA_RUNNING_ = struct__NET_VCA_RUNNING_
