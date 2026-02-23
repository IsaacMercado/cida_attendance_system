from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_pdc_target_info import NET_DVR_PDC_TARGET_INFO


class struct_tagNET_DVR_PDC_TARGET_IN_FRAME(Structure):
    pass

_S(struct_tagNET_DVR_PDC_TARGET_IN_FRAME, [
    ('byTargetNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struTargetInfo', NET_DVR_PDC_TARGET_INFO * 30),
    ('byRes2', BYTE * 8),
])

NET_DVR_PDC_TARGET_IN_FRAME = struct_tagNET_DVR_PDC_TARGET_IN_FRAME
LPNET_DVR_PDC_TARGET_IN_FRAME = POINTER(struct_tagNET_DVR_PDC_TARGET_IN_FRAME)
tagNET_DVR_PDC_TARGET_IN_FRAME = struct_tagNET_DVR_PDC_TARGET_IN_FRAME
