from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_OTHER_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_OTHER_STATUS, [
    ('dwSize', DWORD),
    ('bySirenStatus', BYTE * 8),
    ('byRes', BYTE * 92),
])

NET_DVR_ALARMHOST_OTHER_STATUS = struct_tagNET_DVR_ALARMHOST_OTHER_STATUS
LPNET_DVR_ALARMHOST_OTHER_STATUS = POINTER(struct_tagNET_DVR_ALARMHOST_OTHER_STATUS)
tagNET_DVR_ALARMHOST_OTHER_STATUS = struct_tagNET_DVR_ALARMHOST_OTHER_STATUS
