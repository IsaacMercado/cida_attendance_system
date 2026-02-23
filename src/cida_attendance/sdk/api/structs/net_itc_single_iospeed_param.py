from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_itc_plate_recog_region_param import NET_ITC_PLATE_RECOG_REGION_PARAM


class struct_tagNET_ITC_SINGLE_IOSPEED_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_SINGLE_IOSPEED_PARAM, [
    ('byEnable', BYTE),
    ('byTrigCoil1', BYTE),
    ('byCoil1IOStatus', BYTE),
    ('byTrigCoil2', BYTE),
    ('byCoil2IOStatus', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('byTimeOut', BYTE),
    ('byRelatedIOOutEx', BYTE),
    ('dwDistance', DWORD),
    ('byCapSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('bySpeedCapEn', BYTE),
    ('bySnapTimes1', BYTE),
    ('bySnapTimes2', BYTE),
    ('byBigCarSpeedLimit', BYTE),
    ('byBigCarSignSpeed', BYTE),
    ('byIntervalType', BYTE),
    ('wInterval1', WORD * 4),
    ('wInterval2', WORD * 4),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('byLaneType', BYTE),
    ('byCarSignSpeed', BYTE),
    ('byUseageType', BYTE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_REGION_PARAM * 2),
    ('byRelaLaneDirectionType', BYTE),
    ('byLowSpeedLimit', BYTE),
    ('byBigCarLowSpeedLimit', BYTE),
    ('byLowSpeedCapEn', BYTE),
    ('byEmergencyCapEn', BYTE),
    ('byRes', BYTE * 27),
])

NET_ITC_SINGLE_IOSPEED_PARAM = struct_tagNET_ITC_SINGLE_IOSPEED_PARAM
LPNET_ITC_SINGLE_IOSPEED_PARAM = POINTER(struct_tagNET_ITC_SINGLE_IOSPEED_PARAM)
tagNET_ITC_SINGLE_IOSPEED_PARAM = struct_tagNET_ITC_SINGLE_IOSPEED_PARAM
