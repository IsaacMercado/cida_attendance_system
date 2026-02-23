from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FIRMWARE_VERSION_IFNO(Structure):
    pass

_S(struct_tagNET_DVR_FIRMWARE_VERSION_IFNO, [
    ('dwSize', DWORD),
    ('szFirmwareVersion', c_char * 128),
    ('byRes2', BYTE * 128),
])

NET_DVR_FIRMWARE_VERSION_IFNO = struct_tagNET_DVR_FIRMWARE_VERSION_IFNO
LPNET_DVR_FIRMWARE_VERSION_IFNO = POINTER(struct_tagNET_DVR_FIRMWARE_VERSION_IFNO)
tagNET_DVR_FIRMWARE_VERSION_IFNO = struct_tagNET_DVR_FIRMWARE_VERSION_IFNO
