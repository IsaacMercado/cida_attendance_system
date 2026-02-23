from ctypes import Structure

from ..base_classes import _S, BYTE, SHORT, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_OUTDOOR_UNIT_DEVICEID(Structure):
    pass

_S(struct_tagNET_DVR_OUTDOOR_UNIT_DEVICEID, [
    ('wPeriod', WORD),
    ('wBuildingNumber', WORD),
    ('wUnitNumber', WORD),
    ('wFloorNumber', SHORT),
    ('wDevIndex', WORD),
    ('byRes', BYTE * 118),
])

NET_DVR_OUTDOOR_UNIT_DEVICEID = struct_tagNET_DVR_OUTDOOR_UNIT_DEVICEID
LPNET_DVR_OUTDOOR_UNIT_DEVICEID = POINTER(struct_tagNET_DVR_OUTDOOR_UNIT_DEVICEID)
tagNET_DVR_OUTDOOR_UNIT_DEVICEID = struct_tagNET_DVR_OUTDOOR_UNIT_DEVICEID
