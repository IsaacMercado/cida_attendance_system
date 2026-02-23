from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ALARM_RELATE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ALARM_RELATE_CFG, [
    ('dwSize', DWORD),
    ('dwMaxRelateChanNum', DWORD),
    ('dwRelateChan', DWORD * 512),
    ('byRes1', BYTE * 256),
])

NET_DVR_ALARM_RELATE_CFG = struct_tagNET_DVR_ALARM_RELATE_CFG
LPNET_DVR_ALARM_RELATE_CFG = POINTER(struct_tagNET_DVR_ALARM_RELATE_CFG)
tagNET_DVR_ALARM_RELATE_CFG = struct_tagNET_DVR_ALARM_RELATE_CFG
