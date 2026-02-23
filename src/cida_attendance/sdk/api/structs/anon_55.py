from ctypes import Structure

from ..base_classes import _S, DWORD


class struct_anon_55(Structure):
    pass

_S(struct_anon_55, [
    ('dwEnableCruiseChan', DWORD),
    ('dwCruiseNo', DWORD),
])

NET_DVR_CRUISECHAN_INFO = struct_anon_55
LPNET_DVR_CRUISECHAN_INFO = struct_anon_55
