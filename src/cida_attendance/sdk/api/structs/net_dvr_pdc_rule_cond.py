from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PDC_RULE_COND(Structure):
    pass

_S(struct_tagNET_DVR_PDC_RULE_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('dwID', DWORD),
    ('byRes', BYTE * 60),
])

NET_DVR_PDC_RULE_COND = struct_tagNET_DVR_PDC_RULE_COND
LPNET_DVR_PDC_RULE_COND = POINTER(struct_tagNET_DVR_PDC_RULE_COND)
tagNET_DVR_PDC_RULE_COND = struct_tagNET_DVR_PDC_RULE_COND
