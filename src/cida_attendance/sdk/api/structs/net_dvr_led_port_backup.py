from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LED_PORT_BACKUP(Structure):
    pass

_S(struct_tagNET_DVR_LED_PORT_BACKUP, [
    ('byEnabled', BYTE),
    ('byPortMode', BYTE),
    ('byRes1', BYTE * 2),
    ('dwPairPort', DWORD),
    ('byRes2', BYTE * 16),
])

NET_DVR_LED_PORT_BACKUP = struct_tagNET_DVR_LED_PORT_BACKUP
LPNET_DVR_LED_PORT_BACKUP = POINTER(struct_tagNET_DVR_LED_PORT_BACKUP)
tagNET_DVR_LED_PORT_BACKUP = struct_tagNET_DVR_LED_PORT_BACKUP
