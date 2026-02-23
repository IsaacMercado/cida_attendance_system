from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_stream_info import NET_DVR_STREAM_INFO


class struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE(Structure):
    pass

_S(struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE, [
    ('struStreamInfo', NET_DVR_STREAM_INFO),
    ('wErrCode', WORD),
    ('byRes', BYTE * 30),
])

NET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE = struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE
LPNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE = POINTER(struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE)
tagNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE = struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE
