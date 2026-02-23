from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_PRINTER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_PRINTER_CFG, [
    ('dwSize', DWORD),
    ('byPrinterEnable', BYTE),
    ('byPrintTime', BYTE),
    ('byFaultDetect', BYTE),
    ('byRes1', BYTE),
    ('dwAlarmInfo', DWORD),
    ('dwDeviceInfo', DWORD),
    ('dwOperateInfo', DWORD),
    ('byRes2', BYTE * 256),
])

NET_DVR_ALARMHOST_PRINTER_CFG = struct_tagNET_DVR_ALARMHOST_PRINTER_CFG
LPNET_DVR_ALARMHOST_PRINTER_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_PRINTER_CFG)
tagNET_DVR_ALARMHOST_PRINTER_CFG = struct_tagNET_DVR_ALARMHOST_PRINTER_CFG
