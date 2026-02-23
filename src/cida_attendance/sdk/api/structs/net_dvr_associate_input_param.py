from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ASSOCIATE_INPUT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ASSOCIATE_INPUT_PARAM, [
    ('byEnable', BYTE),
    ('byRes1', BYTE * 3),
    ('dwDeviceIndex', DWORD),
    ('wInputIndex', WORD),
    ('byRes2', BYTE * 18),
])

NET_DVR_ASSOCIATE_INPUT_PARAM = struct_tagNET_DVR_ASSOCIATE_INPUT_PARAM
LPNET_DVR_ASSOCIATE_INPUT_PARAM = POINTER(struct_tagNET_DVR_ASSOCIATE_INPUT_PARAM)
tagNET_DVR_ASSOCIATE_INPUT_PARAM = struct_tagNET_DVR_ASSOCIATE_INPUT_PARAM
