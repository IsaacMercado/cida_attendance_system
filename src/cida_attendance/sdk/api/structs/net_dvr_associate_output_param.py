from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ASSOCIATE_OUTPUT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ASSOCIATE_OUTPUT_PARAM, [
    ('byEnable', BYTE),
    ('byWallNo', BYTE),
    ('byRes1', BYTE * 2),
    ('dwOutputIndex', DWORD),
    ('byRes2', BYTE * 20),
])

NET_DVR_ASSOCIATE_OUTPUT_PARAM = struct_tagNET_DVR_ASSOCIATE_OUTPUT_PARAM
LPNET_DVR_ASSOCIATE_OUTPUT_PARAM = POINTER(struct_tagNET_DVR_ASSOCIATE_OUTPUT_PARAM)
tagNET_DVR_ASSOCIATE_OUTPUT_PARAM = struct_tagNET_DVR_ASSOCIATE_OUTPUT_PARAM
