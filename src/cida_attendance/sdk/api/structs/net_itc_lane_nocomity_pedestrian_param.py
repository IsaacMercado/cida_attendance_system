from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_itc_line import NET_ITC_LINE
from .net_itc_polygon import NET_ITC_POLYGON


class struct_tagNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM, [
    ('byRelatedDriveWay', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('byPedestriansNum', BYTE),
    ('byVehicleSpeed', BYTE),
    ('dwVehicleInterval', DWORD),
    ('byPedesDetRule', BYTE),
    ('byRes', BYTE * 3),
    ('struLaneLine', NET_ITC_LINE),
    ('struStopLine', NET_ITC_LINE),
    ('struPlateRecog', NET_ITC_POLYGON),
    ('byRes1', BYTE * 280),
])

NET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM = struct_tagNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM
LPNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM = POINTER(struct_tagNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM)
tagNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM = struct_tagNET_ITC_LANE_NOCOMITY_PEDESTRIAN_PARAM
