from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MOBILE_CAPTUREPIC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MOBILE_CAPTUREPIC_CFG, [
    ('dwSize', DWORD),
    ('byPreviewFpsAdjMode', BYTE),
    ('bySelPeccType', BYTE),
    ('byOptHabit', BYTE),
    ('byEnablePeccRec', BYTE),
    ('byPicSize', BYTE),
    ('byPicQuality', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_MOBILE_CAPTUREPIC_CFG = struct_tagNET_DVR_MOBILE_CAPTUREPIC_CFG
LPNET_DVR_MOBILE_CAPTUREPIC_CFG = POINTER(struct_tagNET_DVR_MOBILE_CAPTUREPIC_CFG)
tagNET_DVR_MOBILE_CAPTUREPIC_CFG = struct_tagNET_DVR_MOBILE_CAPTUREPIC_CFG
