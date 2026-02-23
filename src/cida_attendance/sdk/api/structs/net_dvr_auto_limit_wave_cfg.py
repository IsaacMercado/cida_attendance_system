from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUTO_LIMIT_WAVE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUTO_LIMIT_WAVE_CFG, [
    ('byFBCEnable', BYTE),
    ('byMode', BYTE),
    ('byFilterQValue', BYTE),
    ('byStaticFilterNum', BYTE),
    ('byRes', BYTE * 16),
])

NET_DVR_AUTO_LIMIT_WAVE_CFG = struct_tagNET_DVR_AUTO_LIMIT_WAVE_CFG
LPNET_DVR_AUTO_LIMIT_WAVE_CFG = POINTER(struct_tagNET_DVR_AUTO_LIMIT_WAVE_CFG)
tagNET_DVR_AUTO_LIMIT_WAVE_CFG = struct_tagNET_DVR_AUTO_LIMIT_WAVE_CFG
