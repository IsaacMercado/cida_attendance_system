from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_subwnd_decode_osd import NET_DVR_SUBWND_DECODE_OSD


class struct_tagNET_DVR_SUBWND_DECODE_OSD_LIST(Structure):
    pass

_S(struct_tagNET_DVR_SUBWND_DECODE_OSD_LIST, [
    ('dwSize', DWORD),
    ('struSubWndList', NET_DVR_SUBWND_DECODE_OSD * 64),
    ('byRes', BYTE * 32),
])

NET_DVR_SUBWND_DECODE_OSD_LIST = struct_tagNET_DVR_SUBWND_DECODE_OSD_LIST
LPNET_DVR_SUBWND_DECODE_OSD_LIST = POINTER(struct_tagNET_DVR_SUBWND_DECODE_OSD_LIST)
tagNET_DVR_SUBWND_DECODE_OSD_LIST = struct_tagNET_DVR_SUBWND_DECODE_OSD_LIST
