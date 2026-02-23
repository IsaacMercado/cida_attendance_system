from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SERIAL_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_SERIAL_CONTROL, [
    ('dwSize', DWORD),
    ('bySerialNum', BYTE),
    ('byRes1', BYTE * 3),
    ('bySerial', BYTE * 32),
    ('byRes2', BYTE * 32),
])

NET_DVR_SERIAL_CONTROL = struct_tagNET_DVR_SERIAL_CONTROL
LPNET_DVR_SERIAL_CONTROL = POINTER(struct_tagNET_DVR_SERIAL_CONTROL)
tagNET_DVR_SERIAL_CONTROL = struct_tagNET_DVR_SERIAL_CONTROL
