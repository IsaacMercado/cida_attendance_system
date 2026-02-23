from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_USING_SERIALPORT(Structure):
    pass

_S(struct_tagNET_DVR_USING_SERIALPORT, [
    ('dwSize', DWORD),
    ('dwSerialPort', DWORD),
    ('byProtocolType', BYTE),
    ('byRes', BYTE * 31),
])

NET_DVR_USING_SERIALPORT = struct_tagNET_DVR_USING_SERIALPORT
LPNET_DVR_USING_SERIALPORT = POINTER(struct_tagNET_DVR_USING_SERIALPORT)
tagNET_DVR_USING_SERIALPORT = struct_tagNET_DVR_USING_SERIALPORT
