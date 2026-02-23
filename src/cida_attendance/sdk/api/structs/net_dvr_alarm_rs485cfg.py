from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_RS485CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_RS485CFG, [
    ('dwSize', DWORD),
    ('sDeviceName', BYTE * 32),
    ('wDeviceType', WORD),
    ('wDeviceProtocol', WORD),
    ('dwBaudRate', DWORD),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('byDuplex', BYTE),
    ('byWorkMode', BYTE),
    ('byChannel', BYTE),
    ('bySerialType', BYTE),
    ('byMode', BYTE),
    ('byOutputDataType', BYTE),
    ('byAddress', BYTE),
    ('byStairsOutputDataType', BYTE),
    ('byRes', BYTE * 32),
])

NET_DVR_ALARM_RS485CFG = struct_tagNET_DVR_ALARM_RS485CFG
LPNET_DVR_ALARM_RS485CFG = POINTER(struct_tagNET_DVR_ALARM_RS485CFG)
tagNET_DVR_ALARM_RS485CFG = struct_tagNET_DVR_ALARM_RS485CFG
