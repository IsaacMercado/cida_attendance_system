from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_reboot_time import NET_DVR_REBOOT_TIME


class struct_tagNET_DVR_AUTO_REBOOT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_AUTO_REBOOT_CFG, [
    ('dwSize', DWORD),
    ('struRebootTime', NET_DVR_REBOOT_TIME),
])

NET_DVR_AUTO_REBOOT_CFG = struct_tagNET_DVR_AUTO_REBOOT_CFG
LPNET_DVR_AUTO_REBOOT_CFG = POINTER(struct_tagNET_DVR_AUTO_REBOOT_CFG)
tagNET_DVR_AUTO_REBOOT_CFG = struct_tagNET_DVR_AUTO_REBOOT_CFG
