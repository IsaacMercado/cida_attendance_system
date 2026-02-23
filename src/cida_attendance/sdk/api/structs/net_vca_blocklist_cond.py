from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, LONG
from ..ctypes_preamble import POINTER
from .net_vca_human_attribute import NET_VCA_HUMAN_ATTRIBUTE


class struct_tagNET_VCA_BLOCKLIST_COND(Structure):
    pass

_S(struct_tagNET_VCA_BLOCKLIST_COND, [
    ('lChannel', LONG),
    ('dwGroupNo', DWORD),
    ('byType', BYTE),
    ('byLevel', BYTE),
    ('byRes1', BYTE * 2),
    ('struAttribute', NET_VCA_HUMAN_ATTRIBUTE),
    ('byRes', BYTE * 20),
])

NET_VCA_BLOCKLIST_COND = struct_tagNET_VCA_BLOCKLIST_COND
LPNET_VCA_BLOCKLIST_COND = POINTER(struct_tagNET_VCA_BLOCKLIST_COND)
tagNET_VCA_BLOCKLIST_COND = struct_tagNET_VCA_BLOCKLIST_COND
