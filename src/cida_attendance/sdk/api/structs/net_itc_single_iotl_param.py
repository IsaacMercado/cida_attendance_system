from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_itc_plate_recog_region_param import NET_ITC_PLATE_RECOG_REGION_PARAM


class struct_tagNET_ITC_SINGLE_IOTL_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SINGLE_IOTL_PARAM, [
    ('byEnable', BYTE),
    ('byLightIO', BYTE),
    ('byTrafficLight', BYTE),
    ('byTrigIO', BYTE),
    ('byTrigIOStatus', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('byRecordEnable', BYTE),
    ('byRecordType', BYTE),
    ('byPreRecordTime', BYTE),
    ('byRecordDelayTime', BYTE),
    ('byRecordTimeOut', BYTE),
    ('byRedSnapTimes', BYTE),
    ('byGreenSnapTimes', BYTE),
    ('byRelatedIOOutEx', BYTE),
    ('byRes1', BYTE),
    ('byIntervalType', BYTE),
    ('wRedInterval', WORD * 4),
    ('wGreenInterval', WORD * 4),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('byRes2', BYTE * 3),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_REGION_PARAM * 2),
    ('byRes', BYTE * 32),
])

NET_ITC_SINGLE_IOTL_PARAM = struct_tagNET_ITC_SINGLE_IOTL_PARAM
LPNET_ITC_SINGLE_IOTL_PARAM = POINTER(struct_tagNET_ITC_SINGLE_IOTL_PARAM)
tagNET_ITC_SINGLE_IOTL_PARAM = struct_tagNET_ITC_SINGLE_IOTL_PARAM
