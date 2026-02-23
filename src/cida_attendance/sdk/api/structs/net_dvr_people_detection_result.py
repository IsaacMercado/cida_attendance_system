from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_people_region import NET_DVR_PEOPLE_REGION
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_PEOPLE_DETECTION_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_PEOPLE_DETECTION_RESULT, [
    ('dwSize', DWORD),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('struPeopleRegion', NET_DVR_PEOPLE_REGION * 8),
    ('byPeopleAlarmType', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_PEOPLE_DETECTION_RESULT = struct_tagNET_DVR_PEOPLE_DETECTION_RESULT
LPNET_DVR_PEOPLE_DETECTION_RESULT = POINTER(struct_tagNET_DVR_PEOPLE_DETECTION_RESULT)
tagNET_DVR_PEOPLE_DETECTION_RESULT = struct_tagNET_DVR_PEOPLE_DETECTION_RESULT
