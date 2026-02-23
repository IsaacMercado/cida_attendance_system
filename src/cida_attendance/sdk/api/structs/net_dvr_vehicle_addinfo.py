from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_llpos_param import NET_DVR_LLPOS_PARAM


class struct_tagNET_DVR_VEHICLE_ADDINFO(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLE_ADDINFO, [
    ('struLLPos', NET_DVR_LLPOS_PARAM),
    ('sVehicleNo', c_char * 64),
    ('byVehicleMonitorTaskID', BYTE * 64),
    ('byUUID', BYTE * 64),
    ('byRes', BYTE * 832),
])

NET_DVR_VEHICLE_ADDINFO = struct_tagNET_DVR_VEHICLE_ADDINFO
LPNET_DVR_VEHICLE_ADDINFO = POINTER(struct_tagNET_DVR_VEHICLE_ADDINFO)
tagNET_DVR_VEHICLE_ADDINFO = struct_tagNET_DVR_VEHICLE_ADDINFO
