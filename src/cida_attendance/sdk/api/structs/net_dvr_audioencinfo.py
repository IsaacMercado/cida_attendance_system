from ctypes import Structure, c_int

from ..base_classes import _S, DWORD


class struct__NET_DVR_AUDIOENCInfo(Structure):
    pass

_S(struct__NET_DVR_AUDIOENCInfo, [
    ('in_frame_size', DWORD),
    ('reserved', c_int * 16),
])

NET_DVR_AUDIOENC_INFO = struct__NET_DVR_AUDIOENCInfo
_NET_DVR_AUDIOENCInfo = struct__NET_DVR_AUDIOENCInfo
