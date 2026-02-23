from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OUTDOOR_FENCE_DEVICEID(Structure):
    pass

_S(struct_tagNET_DVR_OUTDOOR_FENCE_DEVICEID, [
    ('wPeriod', WORD),
    ('wDevIndex', WORD),
    ('byRes', BYTE * 124),
])

NET_DVR_OUTDOOR_FENCE_DEVICEID = struct_tagNET_DVR_OUTDOOR_FENCE_DEVICEID
LPNET_DVR_OUTDOOR_FENCE_DEVICEID = POINTER(struct_tagNET_DVR_OUTDOOR_FENCE_DEVICEID)
tagNET_DVR_OUTDOOR_FENCE_DEVICEID = struct_tagNET_DVR_OUTDOOR_FENCE_DEVICEID
