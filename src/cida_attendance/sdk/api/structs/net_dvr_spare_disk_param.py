from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SPARE_DISK_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SPARE_DISK_PARAM, [
    ('wPDSlot', WORD),
    ('wArrayID', WORD),
    ('bySpareType', BYTE),
    ('byRes', BYTE * 7),
])

NET_DVR_SPARE_DISK_PARAM = struct_tagNET_DVR_SPARE_DISK_PARAM
LPNET_DVR_SPARE_DISK_PARAM = POINTER(struct_tagNET_DVR_SPARE_DISK_PARAM)
tagNET_DVR_SPARE_DISK_PARAM = struct_tagNET_DVR_SPARE_DISK_PARAM
