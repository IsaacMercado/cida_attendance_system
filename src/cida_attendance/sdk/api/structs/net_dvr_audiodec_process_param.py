from ctypes import Structure, c_int, c_ubyte

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_audiodecinfo import NET_DVR_AUDIODEC_INFO


class struct__NET_DVR_AUDIODEC_PROCESS_PARAM(Structure):
    pass

_S(struct__NET_DVR_AUDIODEC_PROCESS_PARAM, [
    ('in_buf', POINTER(c_ubyte)),
    ('out_buf', POINTER(c_ubyte)),
    ('in_data_size', DWORD),
    ('proc_data_size', DWORD),
    ('out_frame_size', DWORD),
    ('dec_info', NET_DVR_AUDIODEC_INFO),
    ('g726dec_reset', c_int),
    ('g711_type', c_int),
    ('reserved', c_int * 16),
])

NET_DVR_AUDIODEC_PROCESS_PARAM = struct__NET_DVR_AUDIODEC_PROCESS_PARAM
_NET_DVR_AUDIODEC_PROCESS_PARAM = struct__NET_DVR_AUDIODEC_PROCESS_PARAM
