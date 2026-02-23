from ctypes import Structure, c_char

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_UPGRADE_IPC_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_UPGRADE_IPC_PARAM, [
    ('struStreamInfo', NET_DVR_STREAM_INFO * int((32 + 32))),
    ('szFileName', c_char * 260),
])

NET_DVR_UPGRADE_IPC_PARAM = struct_tagNET_DVR_UPGRADE_IPC_PARAM
LPNET_DVR_UPGRADE_IPC_PARAM = POINTER(struct_tagNET_DVR_UPGRADE_IPC_PARAM)
tagNET_DVR_UPGRADE_IPC_PARAM = struct_tagNET_DVR_UPGRADE_IPC_PARAM
