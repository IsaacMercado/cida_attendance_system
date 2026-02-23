from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARMHOST_RS485_SLOT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARMHOST_RS485_SLOT_CFG, [
    ('dwSize', DWORD),
    ('sDeviceName', BYTE * 32),
    ('wDeviceType', WORD),
    ('wDeviceProtocol', WORD),
    ('wAddress', WORD),
    ('byChannel', BYTE),
    ('bySlotChan', BYTE),
    ('byRes', BYTE * 60),
])

NET_DVR_ALARMHOST_RS485_SLOT_CFG = struct_tagNET_DVR_ALARMHOST_RS485_SLOT_CFG
LPNET_DVR_ALARMHOST_RS485_SLOT_CFG = POINTER(struct_tagNET_DVR_ALARMHOST_RS485_SLOT_CFG)
tagNET_DVR_ALARMHOST_RS485_SLOT_CFG = struct_tagNET_DVR_ALARMHOST_RS485_SLOT_CFG
