from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_blocklist_info import NET_VCA_BLOCKLIST_INFO


class struct_tagNET_VCA_BLOCKLIST_INFO_ALARM(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_INFO_ALARM, [
    ('struBlockListInfo', NET_VCA_BLOCKLIST_INFO),
    ('dwBlockListPicLen', DWORD),
    ('dwFDIDLen', DWORD),
    ('pFDID', POINTER(BYTE)),
    ('dwPIDLen', DWORD),
    ('pPID', POINTER(BYTE)),
    ('wThresholdValue', WORD),
    ('byIsNoSaveFDPicture', BYTE),
    ('byRealTimeContrast', BYTE),
    ('pBuffer1', POINTER(BYTE)),
])

NET_VCA_BLOCKLIST_INFO_ALARM = struct_tagNET_VCA_BLOCKLIST_INFO_ALARM
LPNET_VCA_BLOCKLIST_INFO_ALARM = POINTER(struct_tagNET_VCA_BLOCKLIST_INFO_ALARM)
tagNET_VCA_BLOCKLIST_INFO_ALARM = struct_tagNET_VCA_BLOCKLIST_INFO_ALARM
