from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_inquest_room_info import NET_DVR_INQUEST_ROOM_INFO
from .net_dvr_inquest_sensor_info import NET_DVR_INQUEST_SENSOR_INFO


class struct_tagNET_DVR_INQUEST_SYSTEM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_SYSTEM_INFO, [
    ('dwRecordMode', DWORD),
    ('dwWorkMode', DWORD),
    ('dwResolutionMode', DWORD),
    ('struSensorInfo', NET_DVR_INQUEST_SENSOR_INFO),
    ('struInquestRoomInfo', NET_DVR_INQUEST_ROOM_INFO * 2),
    ('byEnableHashCheck', BYTE),
    ('byEnableInitCD', BYTE),
    ('byCDProcessingMode', BYTE),
    ('byRes', BYTE * 21),
])

NET_DVR_INQUEST_SYSTEM_INFO = struct_tagNET_DVR_INQUEST_SYSTEM_INFO
LPNET_DVR_INQUEST_SYSTEM_INFO = POINTER(struct_tagNET_DVR_INQUEST_SYSTEM_INFO)
tagNET_DVR_INQUEST_SYSTEM_INFO = struct_tagNET_DVR_INQUEST_SYSTEM_INFO
