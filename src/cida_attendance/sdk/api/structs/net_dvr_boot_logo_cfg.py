from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_BOOT_LOGO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_BOOT_LOGO_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_BOOT_LOGO_CFG = struct_tagNET_DVR_BOOT_LOGO_CFG
LPNET_DVR_BOOT_LOGO_CFG = POINTER(struct_tagNET_DVR_BOOT_LOGO_CFG)
tagNET_DVR_BOOT_LOGO_CFG = struct_tagNET_DVR_BOOT_LOGO_CFG
