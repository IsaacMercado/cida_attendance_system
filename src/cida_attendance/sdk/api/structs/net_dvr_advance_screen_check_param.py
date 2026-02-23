from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ADVANCE_SCREEN_CHECK_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ADVANCE_SCREEN_CHECK_PARAM, [
    ('byDelFullScreenGamut', BYTE),
    ('byDelLightPanelGamut', BYTE),
    ('byDelLightPanelWhiteBalance', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_ADVANCE_SCREEN_CHECK_PARAM = struct_tagNET_DVR_ADVANCE_SCREEN_CHECK_PARAM
LPNET_DVR_ADVANCE_SCREEN_CHECK_PARAM = POINTER(struct_tagNET_DVR_ADVANCE_SCREEN_CHECK_PARAM)
tagNET_DVR_ADVANCE_SCREEN_CHECK_PARAM = struct_tagNET_DVR_ADVANCE_SCREEN_CHECK_PARAM
