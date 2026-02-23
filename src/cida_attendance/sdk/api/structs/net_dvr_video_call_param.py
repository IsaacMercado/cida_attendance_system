from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, SHORT, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VIDEO_CALL_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_VIDEO_CALL_PARAM, [
    ('dwSize', DWORD),
    ('dwCmdType', DWORD),
    ('wPeriod', WORD),
    ('wBuildingNumber', WORD),
    ('wUnitNumber', WORD),
    ('wFloorNumber', SHORT),
    ('wRoomNumber', WORD),
    ('wDevIndex', WORD),
    ('byUnitType', BYTE),
    ('byRes', BYTE * 115),
])

NET_DVR_VIDEO_CALL_PARAM = struct_tagNET_DVR_VIDEO_CALL_PARAM
LPNET_DVR_VIDEO_CALL_PARAM = POINTER(struct_tagNET_DVR_VIDEO_CALL_PARAM)
tagNET_DVR_VIDEO_CALL_PARAM = struct_tagNET_DVR_VIDEO_CALL_PARAM
