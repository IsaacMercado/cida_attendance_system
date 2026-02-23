from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BLOCKLIST_ALARM_RECORD(Structure):
    pass

_S(struct_tagNET_DVR_BLOCKLIST_ALARM_RECORD, [
    ('dwSize', DWORD),
    ('dwSnapFacePicID', DWORD),
    ('dwRegisterID', DWORD),
    ('dwGroupNo', DWORD),
    ('byRes', BYTE * 128),
])

NET_DVR_BLOCKLIST_ALARM_RECORD = struct_tagNET_DVR_BLOCKLIST_ALARM_RECORD
LPNET_DVR_BLOCKLIST_ALARM_RECORD = POINTER(struct_tagNET_DVR_BLOCKLIST_ALARM_RECORD)
tagNET_DVR_BLOCKLIST_ALARM_RECORD = struct_tagNET_DVR_BLOCKLIST_ALARM_RECORD
