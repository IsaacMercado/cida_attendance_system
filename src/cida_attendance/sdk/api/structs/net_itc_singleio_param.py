from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_itc_interval_param import NET_ITC_INTERVAL_PARAM
from .net_itc_plate_recog_region_param import NET_ITC_PLATE_RECOG_REGION_PARAM


class struct_tagNET_ITC_SINGLEIO_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SINGLEIO_PARAM, [
    ('byDefaultStatus', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('bySnapTimes', BYTE),
    ('byRelatedIOOutEx', BYTE),
    ('struInterval', NET_ITC_INTERVAL_PARAM),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('byEnable', BYTE),
    ('byUseageType', BYTE),
    ('byEmergencyCapEn', BYTE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_REGION_PARAM * 2),
    ('byRes', BYTE * 24),
])

NET_ITC_SINGLEIO_PARAM = struct_tagNET_ITC_SINGLEIO_PARAM
LPNET_ITC_SINGLEIO_PARAM = POINTER(struct_tagNET_ITC_SINGLEIO_PARAM)
tagNET_ITC_SINGLEIO_PARAM = struct_tagNET_ITC_SINGLEIO_PARAM
