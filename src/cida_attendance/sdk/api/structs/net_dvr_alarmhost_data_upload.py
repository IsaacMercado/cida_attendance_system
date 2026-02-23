from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_alarmhost_data_union import NET_DVR_ALARMHOST_DATA_UNION


class struct_tagNET_DVR_ALARMHOST_DATA_UPLOAD(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_DATA_UPLOAD, [
    ('dwSize', DWORD),
    ('byDataType', BYTE),
    ('byRes1', BYTE * 3),
    ('struAlarmData', NET_DVR_ALARMHOST_DATA_UNION),
    ('byRes2', BYTE * 32),
])

NET_DVR_ALARMHOST_DATA_UPLOAD = struct_tagNET_DVR_ALARMHOST_DATA_UPLOAD
LPNET_DVR_ALARMHOST_DATA_UPLOAD = POINTER(struct_tagNET_DVR_ALARMHOST_DATA_UPLOAD)
tagNET_DVR_ALARMHOST_DATA_UPLOAD = struct_tagNET_DVR_ALARMHOST_DATA_UPLOAD
