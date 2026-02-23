from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_vehicleflow_info import NET_DVR_VEHICLEFLOW_INFO


class struct_tagNET_DVR_VEHICLEFLOW_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VEHICLEFLOW_CFG, [
    ('dwSize', DWORD),
    ('struVehFlow', NET_DVR_VEHICLEFLOW_INFO * 24),
    ('byRes', BYTE * 512),
])

NET_DVR_VEHICLEFLOW_CFG = struct_tagNET_DVR_VEHICLEFLOW_CFG
LPNET_DVR_VEHICLEFLOW_CFG = POINTER(struct_tagNET_DVR_VEHICLEFLOW_CFG)
tagNET_DVR_VEHICLEFLOW_CFG = struct_tagNET_DVR_VEHICLEFLOW_CFG
