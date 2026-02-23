from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_vca_line import NET_VCA_LINE


class struct_tagNET_DVR_PDC_LINE_CALIBRATION(Structure):
    pass

_S(struct_tagNET_DVR_PDC_LINE_CALIBRATION, [
    ('struCalibrationLine', NET_VCA_LINE),
    ('byRes', BYTE * 224),
])

NET_DVR_PDC_LINE_CALIBRATION = struct_tagNET_DVR_PDC_LINE_CALIBRATION
LPNET_DVR_PDC_LINE_CALIBRATION = POINTER(struct_tagNET_DVR_PDC_LINE_CALIBRATION)
tagNET_DVR_PDC_LINE_CALIBRATION = struct_tagNET_DVR_PDC_LINE_CALIBRATION
