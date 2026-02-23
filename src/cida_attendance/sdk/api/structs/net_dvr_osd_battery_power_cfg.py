from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_point import NET_VCA_POINT


class struct_tagNET_DVR_OSD_BATTERY_POWER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_OSD_BATTERY_POWER_CFG, [
    ('dwSize', DWORD),
    ('struOSDBatteryPower', NET_VCA_POINT),
    ('byOSDBatteryPower', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_OSD_BATTERY_POWER_CFG = struct_tagNET_DVR_OSD_BATTERY_POWER_CFG
LPNET_DVR_OSD_BATTERY_POWER_CFG = POINTER(struct_tagNET_DVR_OSD_BATTERY_POWER_CFG)
tagNET_DVR_OSD_BATTERY_POWER_CFG = struct_tagNET_DVR_OSD_BATTERY_POWER_CFG
