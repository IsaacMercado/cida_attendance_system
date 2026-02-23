from ctypes import Structure

from ..base_classes import _S, DWORD


class struct_anon_56(Structure):
    pass

_S(struct_anon_56, [
    ('dwEnablePtzTrackChan', DWORD),
    ('dwPtzTrackNo', DWORD),
])

NET_DVR_PTZTRACKCHAN_INFO = struct_anon_56
LPNET_DVR_PTZTRACKCHAN_INFO = struct_anon_56
