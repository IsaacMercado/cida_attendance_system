from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MAINBOARD_SERIAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MAINBOARD_SERIAL_CFG, [
    ('dwSize', DWORD),
    ('bySerialWorkMode', BYTE),
    ('byFunType', BYTE),
    ('byDataBit', BYTE),
    ('byStopBit', BYTE),
    ('dwBaudRate', DWORD),
    ('byParity', BYTE),
    ('byFlowcontrol', BYTE),
    ('wProtocol', WORD),
    ('byVariable', BYTE),
    ('byGateWayEnable', BYTE),
    ('byRes', BYTE * 30),
])

NET_DVR_MAINBOARD_SERIAL_CFG = struct_tagNET_DVR_MAINBOARD_SERIAL_CFG
LPNET_DVR_MAINBOARD_SERIAL_CFG = POINTER(struct_tagNET_DVR_MAINBOARD_SERIAL_CFG)
tagNET_DVR_MAINBOARD_SERIAL_CFG = struct_tagNET_DVR_MAINBOARD_SERIAL_CFG
