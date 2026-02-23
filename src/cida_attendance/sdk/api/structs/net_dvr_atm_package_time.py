from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_osd_position import NET_DVR_OSD_POSITION
from .net_dvr_package_location import NET_DVR_PACKAGE_LOCATION
from .net_dvrt_time_format import NET_DVR_TIME_FORMAT


class struct_tagNET_DVR_ATM_PACKAGE_TIME(Structure):
    pass

_S(struct_tagNET_DVR_ATM_PACKAGE_TIME, [
    ('location', NET_DVR_PACKAGE_LOCATION),
    ('struTimeForm', NET_DVR_TIME_FORMAT),
    ('struOsdPosition', NET_DVR_OSD_POSITION),
    ('byRes', BYTE * 8),
])

NET_DVR_ATM_PACKAGE_TIME = struct_tagNET_DVR_ATM_PACKAGE_TIME
LPNET_DVR_ATM_PACKAGE_TIME = POINTER(struct_tagNET_DVR_ATM_PACKAGE_TIME)
tagNET_DVR_ATM_PACKAGE_TIME = struct_tagNET_DVR_ATM_PACKAGE_TIME
