from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_human_attribute import NET_VCA_HUMAN_ATTRIBUTE


class struct_tagNET_VCA_BLOCKLIST_INFO(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_INFO, [
    ('dwSize', DWORD),
    ('dwRegisterID', DWORD),
    ('dwGroupNo', DWORD),
    ('byType', BYTE),
    ('byLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('struAttribute', NET_VCA_HUMAN_ATTRIBUTE),
    ('byRemark', BYTE * 32),
    ('dwFDDescriptionLen', DWORD),
    ('pFDDescriptionBuffer', POINTER(BYTE)),
    ('dwFCAdditionInfoLen', DWORD),
    ('pFCAdditionInfoBuffer', POINTER(BYTE)),
    ('dwThermalDataLen', DWORD),
])

NET_VCA_BLOCKLIST_INFO = struct_tagNET_VCA_BLOCKLIST_INFO
LPNET_VCA_BLOCKLIST_INFO = POINTER(struct_tagNET_VCA_BLOCKLIST_INFO)
tagNET_VCA_BLOCKLIST_INFO = struct_tagNET_VCA_BLOCKLIST_INFO
