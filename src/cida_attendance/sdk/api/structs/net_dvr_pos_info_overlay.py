from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_POS_INFO_OVERLAY(Structure):
    pass

_S(struct_tagNET_DVR_POS_INFO_OVERLAY, [
    ('dwSize', DWORD),
    ('byPosInfoOverlayEnable', BYTE),
    ('byOverlayType', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_POS_INFO_OVERLAY = struct_tagNET_DVR_POS_INFO_OVERLAY
LPNET_DVR_POS_INFO_OVERLAY = POINTER(struct_tagNET_DVR_POS_INFO_OVERLAY)
tagNET_DVR_POS_INFO_OVERLAY = struct_tagNET_DVR_POS_INFO_OVERLAY
