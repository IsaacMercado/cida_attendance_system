from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_USB_RS232(Structure):
    pass

_S(struct_tagNET_DVR_USB_RS232, [
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('byVirtualSerialPort', BYTE),
    ('byRes', BYTE * 3),
])

NET_DVR_USB_RS232 = struct_tagNET_DVR_USB_RS232
LPNET_DVR_USB_RS232 = POINTER(struct_tagNET_DVR_USB_RS232)
tagNET_DVR_USB_RS232 = struct_tagNET_DVR_USB_RS232
