from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VEHICLEFLOW_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLEFLOW_INFO, [
    ('dwVehicleFlowValue', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_VEHICLEFLOW_INFO = struct_tagNET_DVR_VEHICLEFLOW_INFO
LPNET_DVR_VEHICLEFLOW_INFO = POINTER(struct_tagNET_DVR_VEHICLEFLOW_INFO)
tagNET_DVR_VEHICLEFLOW_INFO = struct_tagNET_DVR_VEHICLEFLOW_INFO
