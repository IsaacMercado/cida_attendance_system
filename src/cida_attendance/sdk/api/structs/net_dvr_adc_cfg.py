from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ADC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ADC_CFG, [
    ('byGainR', BYTE),
    ('byGainG', BYTE),
    ('byGainB', BYTE),
    ('byOffsetR', BYTE),
    ('byOffsetG', BYTE),
    ('byOffsetB', BYTE),
    ('byRes', BYTE * 6),
])

NET_DVR_ADC_CFG = struct_tagNET_DVR_ADC_CFG
LPNET_DVR_ADC_CFG = POINTER(struct_tagNET_DVR_ADC_CFG)
tagNET_DVR_ADC_CFG = struct_tagNET_DVR_ADC_CFG
