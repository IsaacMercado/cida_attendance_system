from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_structhead import NET_DVR_STRUCTHEAD


class struct_tagNET_DVR_POS_INFO(Structure):
    pass

_S(struct_tagNET_DVR_POS_INFO, [
    ('struVerHead', NET_DVR_STRUCTHEAD),
    ('dwChannelNum', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_POS_INFO = struct_tagNET_DVR_POS_INFO
LPNET_DVR_POS_INFO = POINTER(struct_tagNET_DVR_POS_INFO)
tagNET_DVR_POS_INFO = struct_tagNET_DVR_POS_INFO
