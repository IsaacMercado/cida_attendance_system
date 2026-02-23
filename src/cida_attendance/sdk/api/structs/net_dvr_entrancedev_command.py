from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ENTRANCEDEV_COMMAND(Structure):
    pass

_S(struct_tagNET_DVR_ENTRANCEDEV_COMMAND, [
    ('dwSize', DWORD),
    ('byDevCtrlCode', BYTE),
    ('byManualIssuedData', BYTE),
    ('byRes', BYTE * 62),
])

NET_DVR_ENTRANCEDEV_COMMAND = struct_tagNET_DVR_ENTRANCEDEV_COMMAND
LPNET_DVR_ENTRANCEDEV_COMMAND = POINTER(struct_tagNET_DVR_ENTRANCEDEV_COMMAND)
tagNET_DVR_ENTRANCEDEV_COMMAND = struct_tagNET_DVR_ENTRANCEDEV_COMMAND
