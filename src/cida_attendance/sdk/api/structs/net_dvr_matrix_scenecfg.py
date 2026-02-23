from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_SCENECFG(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_SCENECFG, [
    ('dwSize', DWORD),
    ('sSceneName', BYTE * 32),
    ('byBigScreenNums', BYTE),
    ('byRes1', BYTE * 3),
    ('wDecChanNums', WORD),
    ('wDispChanNums', WORD),
    ('byRes2', BYTE * 12),
    ('pBigScreenBuffer', POINTER(BYTE)),
    ('pDecChanBuffer', POINTER(BYTE)),
    ('pDispChanBuffer', POINTER(BYTE)),
])

NET_DVR_MATRIX_SCENECFG = struct_tagNET_DVR_MATRIX_SCENECFG
LPNET_DVR_MATRIX_SCENECFG = POINTER(struct_tagNET_DVR_MATRIX_SCENECFG)
tagNET_DVR_MATRIX_SCENECFG = struct_tagNET_DVR_MATRIX_SCENECFG
