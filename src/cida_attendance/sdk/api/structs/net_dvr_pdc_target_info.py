from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_PDC_TARGET_INFO(Structure):
    pass

_S(struct_tagNET_DVR_PDC_TARGET_INFO, [
    ('dwTargetID', DWORD),
    ('struTargetRect', NET_VCA_RECT),
    ('byRes1', BYTE * 8),
])

NET_DVR_PDC_TARGET_INFO = struct_tagNET_DVR_PDC_TARGET_INFO
LPNET_DVR_PDC_TARGET_INFO = POINTER(struct_tagNET_DVR_PDC_TARGET_INFO)
tagNET_DVR_PDC_TARGET_INFO = struct_tagNET_DVR_PDC_TARGET_INFO
