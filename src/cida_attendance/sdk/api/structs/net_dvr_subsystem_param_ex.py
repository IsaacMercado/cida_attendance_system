from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_remind_time import NET_DVR_REMIND_TIME


class struct_tagNET_DVR_SUBSYSTEM_PARAM_EX(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEM_PARAM_EX, [
    ('dwSize', DWORD),
    ('struAlarmTime', (NET_DVR_SCHEDTIME * 8) * 7),
    ('byAlarmInAdvance', BYTE),
    ('byRes1', BYTE * 3),
    ('byJointAlarmIn', BYTE * int((512 / 8))),
    ('byJointKeyboard', BYTE * int((64 / 8))),
    ('byJointOpetaterUser', BYTE * int((256 / 8))),
    ('struAlarmRemindTime', (NET_DVR_REMIND_TIME * 8) * 7),
    ('byJointNetUser', BYTE * int((64 / 8))),
    ('byRes2', BYTE * 280),
])

NET_DVR_SUBSYSTEM_PARAM_EX = struct_tagNET_DVR_SUBSYSTEM_PARAM_EX
LPNET_DVR_SUBSYSTEM_PARAM_EX = POINTER(struct_tagNET_DVR_SUBSYSTEM_PARAM_EX)
tagNET_DVR_SUBSYSTEM_PARAM_EX = struct_tagNET_DVR_SUBSYSTEM_PARAM_EX
