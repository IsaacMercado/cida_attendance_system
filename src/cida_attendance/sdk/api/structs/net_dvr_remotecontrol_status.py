from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REMOTECONTROL_STATUS_(Structure):
    pass

_S(struct_tagNET_DVR_REMOTECONTROL_STATUS_, [
    ('dwSize', DWORD),
    ('byAlarmStatus', BYTE),
    ('byRes', BYTE * 3),
    ('wAlarmDealyTime', WORD),
    ('wDisAlarmDealyTime', WORD),
    ('byRes1', BYTE * 64),
])

NET_DVR_REMOTECONTROL_STATUS = struct_tagNET_DVR_REMOTECONTROL_STATUS_
LPNET_DVR_REMOTECONTROL_STATUS = POINTER(struct_tagNET_DVR_REMOTECONTROL_STATUS_)
tagNET_DVR_REMOTECONTROL_STATUS_ = struct_tagNET_DVR_REMOTECONTROL_STATUS_
