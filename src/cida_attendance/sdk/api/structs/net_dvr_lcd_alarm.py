from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LCD_ALARM(Structure):
    pass

_S(struct_tagNET_DVR_LCD_ALARM, [
    ('dwSize', DWORD),
    ('dwScreenID', DWORD),
    ('byOnOffLine', BYTE),
    ('byTempState', BYTE),
    ('byFanState', BYTE),
    ('byFanException', BYTE),
    ('byTemperature', BYTE),
    ('byRes', BYTE * 27),
])

NET_DVR_LCD_ALARM = struct_tagNET_DVR_LCD_ALARM
LPNET_DVR_LCD_ALARM = POINTER(struct_tagNET_DVR_LCD_ALARM)
tagNET_DVR_LCD_ALARM = struct_tagNET_DVR_LCD_ALARM
