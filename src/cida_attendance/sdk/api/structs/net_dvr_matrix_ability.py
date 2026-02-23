from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_ABILITY(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_ABILITY, [
    ('dwSize', DWORD),
    ('byDecNums', BYTE),
    ('byStartChan', BYTE),
    ('byVGANums', BYTE),
    ('byBNCNums', BYTE),
    ('byVGAWindowMode', (BYTE * 12) * 8),
    ('byBNCWindowMode', BYTE * 4),
    ('byDspNums', BYTE),
    ('byHDMINums', BYTE),
    ('byDVINums', BYTE),
    ('byRes1', BYTE * 13),
    ('bySupportResolution', BYTE * 64),
    ('byHDMIWindowMode', (BYTE * 8) * 4),
    ('byDVIWindowMode', (BYTE * 8) * 4),
    ('byRes2', BYTE * 24),
])

NET_DVR_MATRIX_ABILITY = struct_tagNET_DVR_MATRIX_ABILITY
LPNET_DVR_MATRIX_ABILITY = POINTER(struct_tagNET_DVR_MATRIX_ABILITY)
tagNET_DVR_MATRIX_ABILITY = struct_tagNET_DVR_MATRIX_ABILITY
