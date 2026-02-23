from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INQUEST_SENSOR_DEVICE(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_SENSOR_DEVICE, [
    ('wDeviceType', WORD),
    ('wDeviceAddr', WORD),
    ('byRes', BYTE * 28),
])

NET_DVR_INQUEST_SENSOR_DEVICE = struct_tagNET_DVR_INQUEST_SENSOR_DEVICE
LPNET_DVR_INQUEST_SENSOR_DEVICE = POINTER(struct_tagNET_DVR_INQUEST_SENSOR_DEVICE)
tagNET_DVR_INQUEST_SENSOR_DEVICE = struct_tagNET_DVR_INQUEST_SENSOR_DEVICE
