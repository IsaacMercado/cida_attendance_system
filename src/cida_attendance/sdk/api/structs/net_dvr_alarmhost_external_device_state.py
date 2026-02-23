from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_external_device_state_union import NET_DVR_EXTERNAL_DEVICE_STATE_UNION


class struct_tagNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE, [
    ('dwSize', DWORD),
    ('byDevType', BYTE),
    ('byRes1', BYTE * 3),
    ('struDevState', NET_DVR_EXTERNAL_DEVICE_STATE_UNION),
    ('byRes2', BYTE * 32),
])

NET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE = struct_tagNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE
LPNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE = POINTER(struct_tagNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE)
tagNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE = struct_tagNET_DVR_ALARMHOST_EXTERNAL_DEVICE_STATE
