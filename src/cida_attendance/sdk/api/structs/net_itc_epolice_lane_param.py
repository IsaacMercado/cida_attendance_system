from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_itc_plate_recog_region_param import NET_ITC_PLATE_RECOG_REGION_PARAM
from .net_itc_serial_info import NET_ITC_SERIAL_INFO


class struct_tagNET_ITC_EPOLICE_LANE_PARAM(Structure):
    pass

_S(struct_tagNET_ITC_EPOLICE_LANE_PARAM, [
    ('byEnable', BYTE),
    ('byRelatedDriveWay', BYTE),
    ('wDistance', WORD),
    ('byRecordEnable', BYTE),
    ('byRecordType', BYTE),
    ('byPreRecordTime', BYTE),
    ('byRecordDelayTime', BYTE),
    ('byRecordTimeOut', BYTE),
    ('bySignSpeed', BYTE),
    ('bySpeedLimit', BYTE),
    ('byOverlayDriveWay', BYTE),
    ('struSerialInfo', NET_ITC_SERIAL_INFO),
    ('byRelatedIOOut', BYTE * 4),
    ('byFlashMode', BYTE),
    ('bySerialType', BYTE),
    ('byRelatedIOOutEx', BYTE),
    ('bySnapPicPreRecord', BYTE),
    ('struPlateRecog', NET_ITC_PLATE_RECOG_REGION_PARAM * 2),
    ('byBigCarSignSpeed', BYTE),
    ('byBigCarSpeedLimit', BYTE),
    ('byRedTrafficLightChan', BYTE),
    ('byYellowTrafficLightChan', BYTE),
    ('byRelaLaneDirectionType', BYTE),
    ('byRes3', BYTE * 11),
])

NET_ITC_EPOLICE_LANE_PARAM = struct_tagNET_ITC_EPOLICE_LANE_PARAM
LPNET_ITC_EPOLICE_LANE_PARAM = POINTER(struct_tagNET_ITC_EPOLICE_LANE_PARAM)
tagNET_ITC_EPOLICE_LANE_PARAM = struct_tagNET_ITC_EPOLICE_LANE_PARAM
