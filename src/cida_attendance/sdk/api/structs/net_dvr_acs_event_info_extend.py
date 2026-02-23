from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND(Structure):
    pass

_S(struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND, [
    ('dwFrontSerialNo', DWORD),
    ('byUserType', BYTE),
    ('byCurrentVerifyMode', BYTE),
    ('byCurrentEvent', BYTE),
    ('byPurePwdVerifyEnable', BYTE),
    ('byEmployeeNo', BYTE * 32),
    ('byAttendanceStatus', BYTE),
    ('byStatusValue', BYTE),
    ('byRes2', BYTE * 2),
    ('byUUID', BYTE * 36),
    ('byDeviceName', BYTE * 64),
    ('byRes', BYTE * 24),
])

NET_DVR_ACS_EVENT_INFO_EXTEND = struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND
LPNET_DVR_ACS_EVENT_INFO_EXTEND = POINTER(struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND)
tagNET_DVR_ACS_EVENT_INFO_EXTEND = struct_tagNET_DVR_ACS_EVENT_INFO_EXTEND
