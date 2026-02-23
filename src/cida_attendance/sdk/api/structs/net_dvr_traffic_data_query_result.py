from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_traffic_picture_param import NET_DVR_TRAFFIC_PICTURE_PARAM


class struct_tagNET_DVR_TRAFFIC_DATA_QUERY_RESULT_(Structure):
    pass

_S(struct_tagNET_DVR_TRAFFIC_DATA_QUERY_RESULT_, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('sLicense', c_char * 16),
    ('dwPlateType', DWORD),
    ('dwPlateColor', DWORD),
    ('dwVehicleColor', DWORD),
    ('dwVehicleType', DWORD),
    ('dwIllegalType', DWORD),
    ('dwEventType', DWORD),
    ('dwForensiceType', DWORD),
    ('wVehicleLogoRecog', WORD),
    ('byLaneNo', BYTE),
    ('byDirection', BYTE),
    ('wSpeed', WORD),
    ('byDataType', BYTE),
    ('byRes', BYTE * 253),
    ('struTrafficPic', NET_DVR_TRAFFIC_PICTURE_PARAM * 8),
])

NET_DVR_TRAFFIC_DATA_QUERY_RESULT = struct_tagNET_DVR_TRAFFIC_DATA_QUERY_RESULT_
LPNET_DVR_TRAFFIC_DATA_QUERY_RESULT = POINTER(struct_tagNET_DVR_TRAFFIC_DATA_QUERY_RESULT_)
tagNET_DVR_TRAFFIC_DATA_QUERY_RESULT_ = struct_tagNET_DVR_TRAFFIC_DATA_QUERY_RESULT_
