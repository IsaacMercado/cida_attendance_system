from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOSTDIALSETUPMODE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOSTDIALSETUPMODE, [
    ('dwSize', DWORD),
    ('byEnableMode', BYTE),
    ('byCallType', BYTE),
    ('byRes1', BYTE * 14),
])

NET_DVR_ALARMHOSTDIALSETUPMODE = struct_tagNET_DVR_ALARMHOSTDIALSETUPMODE
LPNET_DVR_ALARMHOSTDIALSETUPMODE = POINTER(struct_tagNET_DVR_ALARMHOSTDIALSETUPMODE)
tagNET_DVR_ALARMHOSTDIALSETUPMODE = struct_tagNET_DVR_ALARMHOSTDIALSETUPMODE
