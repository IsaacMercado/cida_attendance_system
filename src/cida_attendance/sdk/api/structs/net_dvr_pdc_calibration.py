from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_rect_list import NET_DVR_RECT_LIST


class struct_tagNET_DVR_PDC_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_PDC_CALIBRATION, [
    ('struRectList', NET_DVR_RECT_LIST),
    ('byRes', BYTE * 120),
])

NET_DVR_PDC_CALIBRATION = struct_tagNET_DVR_PDC_CALIBRATION
LPNET_DVR_PDC_CALIBRATION = POINTER(struct_tagNET_DVR_PDC_CALIBRATION)
tagNET_DVR_PDC_CALIBRATION = struct_tagNET_DVR_PDC_CALIBRATION
