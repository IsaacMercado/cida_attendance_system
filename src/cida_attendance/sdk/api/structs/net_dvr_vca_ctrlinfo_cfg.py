from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VCA_CTRLINFO_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VCA_CTRLINFO_CFG, [
    ('dwSize', DWORD),
    ('byVCAEnable', BYTE),
    ('byVCAType', BYTE),
    ('byStreamWithVCA', BYTE),
    ('byMode', BYTE),
    ('byControlType', BYTE),
    ('byRes1', BYTE * 3),
    ('wRelatedChannel', WORD * 4),
    ('byRes', BYTE * 72),
])

NET_DVR_VCA_CTRLINFO_CFG = struct_tagNET_DVR_VCA_CTRLINFO_CFG
LPNET_DVR_VCA_CTRLINFO_CFG = POINTER(struct_tagNET_DVR_VCA_CTRLINFO_CFG)
tagNET_DVR_VCA_CTRLINFO_CFG = struct_tagNET_DVR_VCA_CTRLINFO_CFG
