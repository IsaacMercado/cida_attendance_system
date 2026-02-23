from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_osd_info import NET_DVR_OSD_INFO


class struct_tagNET_DVR_DECODE_CHANNEL_OSD(Structure):
    pass

_S(struct_tagNET_DVR_DECODE_CHANNEL_OSD, [
    ('dwSize', DWORD),
    ('struOSDInfo', NET_DVR_OSD_INFO * 8),
    ('byRes', BYTE * 32),
])

NET_DVR_DECODE_CHANNEL_OSD = struct_tagNET_DVR_DECODE_CHANNEL_OSD
LPNET_DVR_DECODE_CHANNEL_OSD = POINTER(struct_tagNET_DVR_DECODE_CHANNEL_OSD)
tagNET_DVR_DECODE_CHANNEL_OSD = struct_tagNET_DVR_DECODE_CHANNEL_OSD
