from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CAMERACHAN_SERIALCFG(Structure):
    pass

_S(struct_tagNET_DVR_CAMERACHAN_SERIALCFG, [
    ('dwSize', DWORD),
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('wPTZProtocol', WORD),
    ('byRes1', BYTE * 6),
    ('dwSerialPort', DWORD),
    ('bySerialAddress', BYTE),
    ('byRes', BYTE * 15),
])

NET_DVR_CAMERACHAN_SERIALCFG = struct_tagNET_DVR_CAMERACHAN_SERIALCFG
LPNET_DVR_CAMERACHAN_SERIALCFG = POINTER(struct_tagNET_DVR_CAMERACHAN_SERIALCFG)
tagNET_DVR_CAMERACHAN_SERIALCFG = struct_tagNET_DVR_CAMERACHAN_SERIALCFG
