from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PLATERECOG_PARA(Structure):
    pass

_S(struct_tagNET_DVR_PLATERECOG_PARA, [
    ('dwSize', DWORD),
    ('byPrMode', BYTE),
    ('byPrScene', BYTE),
    ('byPrDetRect', BYTE),
    ('byPrPicQuality', BYTE),
    ('byPrPicMode', BYTE),
    ('byPlateOsdDisplay', BYTE),
    ('byPrProvCharIndex', BYTE),
    ('byPrProvCharIndex1', BYTE),
    ('byPrProvCharIndex2', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_PLATERECOG_PARA = struct_tagNET_DVR_PLATERECOG_PARA
LPNET_DVR_PLATERECOG_PARA = POINTER(struct_tagNET_DVR_PLATERECOG_PARA)
tagNET_DVR_PLATERECOG_PARA = struct_tagNET_DVR_PLATERECOG_PARA
