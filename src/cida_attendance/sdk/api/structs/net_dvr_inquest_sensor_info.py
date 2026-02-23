from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_inquest_sensor_device import NET_DVR_INQUEST_SENSOR_DEVICE


class struct_tagNET_DVR_INQUEST_SENSOR_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_SENSOR_INFO, [
    ('struSensorDevice', NET_DVR_INQUEST_SENSOR_DEVICE * 2),
    ('dwSupportPro', DWORD),
    ('byRes', BYTE * 120),
])

NET_DVR_INQUEST_SENSOR_INFO = struct_tagNET_DVR_INQUEST_SENSOR_INFO
LPNET_DVR_INQUEST_SENSOR_INFO = POINTER(struct_tagNET_DVR_INQUEST_SENSOR_INFO)
tagNET_DVR_INQUEST_SENSOR_INFO = struct_tagNET_DVR_INQUEST_SENSOR_INFO
