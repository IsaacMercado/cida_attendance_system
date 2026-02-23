from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_VCA_CTRLINFO_COND(Structure):
    pass

_S(struct_tagNET_DVR_VCA_CTRLINFO_COND, [
    ('dwSize', DWORD),
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('byRes', BYTE * 64),
])

NET_DVR_VCA_CTRLINFO_COND = struct_tagNET_DVR_VCA_CTRLINFO_COND
LPNET_DVR_VCA_CTRLINFO_COND = POINTER(struct_tagNET_DVR_VCA_CTRLINFO_COND)
tagNET_DVR_VCA_CTRLINFO_COND = struct_tagNET_DVR_VCA_CTRLINFO_COND
