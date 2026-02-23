from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_REBOOT_TIME(Structure):
    pass

_S(struct_tagNET_DVR_REBOOT_TIME, [
    ('byDate', BYTE),
    ('byHour', BYTE),
    ('byMinute', BYTE),
    ('byRes1', BYTE),
    ('byRebootMode', BYTE),
    ('byDisabled', BYTE),
    ('byRes', BYTE * 10),
])

NET_DVR_REBOOT_TIME = struct_tagNET_DVR_REBOOT_TIME
LPNET_DVR_REBOOT_TIME = POINTER(struct_tagNET_DVR_REBOOT_TIME)
tagNET_DVR_REBOOT_TIME = struct_tagNET_DVR_REBOOT_TIME
