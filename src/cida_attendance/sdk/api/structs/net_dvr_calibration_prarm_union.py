from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_behavior_in_calibration import NET_DVR_BEHAVIOR_IN_CALIBRATION
from .net_dvr_behavior_out_calibration import NET_DVR_BEHAVIOR_OUT_CALIBRATION
from .net_dvr_bv_direct_calibration import NET_DVR_BV_DIRECT_CALIBRATION
from .net_dvr_its_calibration import NET_DVR_ITS_CALIBRATION
from .net_dvr_pdc_calibration import NET_DVR_PDC_CALIBRATION
from .net_dvr_pdc_line_calibration import NET_DVR_PDC_LINE_CALIBRATION


class union_tagNET_DVR_CALIBRATION_PRARM_UNION(Union):
    pass

_S(union_tagNET_DVR_CALIBRATION_PRARM_UNION, [
    ('byRes', BYTE * 240),
    ('struPDCCalibration', NET_DVR_PDC_CALIBRATION),
    ('struBehaviorOutCalibration', NET_DVR_BEHAVIOR_OUT_CALIBRATION),
    ('struBehaviorInCalibration', NET_DVR_BEHAVIOR_IN_CALIBRATION),
    ('struITSCalibration', NET_DVR_ITS_CALIBRATION),
    ('struBvDirectCalibration', NET_DVR_BV_DIRECT_CALIBRATION),
    ('struPDCLineCalibration', NET_DVR_PDC_LINE_CALIBRATION),
])

NET_DVR_CALIBRATION_PRARM_UNION = union_tagNET_DVR_CALIBRATION_PRARM_UNION
LPNET_DVR_CALIBRATION_PRARM_UNION = POINTER(union_tagNET_DVR_CALIBRATION_PRARM_UNION)
tagNET_DVR_CALIBRATION_PRARM_UNION = union_tagNET_DVR_CALIBRATION_PRARM_UNION
