from ctypes import Structure, c_int

from ..base_classes import _S


class struct__NET_DVR_AUDIODECInfo(Structure):
    pass

_S(struct__NET_DVR_AUDIODECInfo, [
    ('nchans', c_int),
    ('sample_rate', c_int),
    ('aacdec_profile', c_int),
    ('reserved', c_int * 16),
])

NET_DVR_AUDIODEC_INFO = struct__NET_DVR_AUDIODECInfo
_NET_DVR_AUDIODECInfo = struct__NET_DVR_AUDIODECInfo
