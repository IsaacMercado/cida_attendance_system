from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_REGISTOR_VALUE(Structure):
    pass

_S(struct_tagNET_DVR_LED_REGISTOR_VALUE, [
    ('byChip1High', BYTE),
    ('byChip1Low', BYTE),
    ('byChip2High', BYTE),
    ('byChip2Low', BYTE),
    ('byChip3High', BYTE),
    ('byChip3Low', BYTE),
    ('byChip4High', BYTE),
    ('byChip4Low', BYTE),
    ('byChip5High', BYTE),
    ('byChip5Low', BYTE),
    ('byChip6High', BYTE),
    ('byChip6Low', BYTE),
    ('byRes', BYTE * 4),
])

NET_DVR_LED_REGISTOR_VALUE = struct_tagNET_DVR_LED_REGISTOR_VALUE
LPNET_DVR_LED_REGISTOR_VALUE = POINTER(struct_tagNET_DVR_LED_REGISTOR_VALUE)
tagNET_DVR_LED_REGISTOR_VALUE = struct_tagNET_DVR_LED_REGISTOR_VALUE
