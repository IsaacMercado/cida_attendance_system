from ctypes import Structure, c_float, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_llpos_param import NET_DVR_LLPOS_PARAM
from .net_dvr_time_ex import NET_DVR_TIME_EX
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_VCA_FACESNAP_ADDINFO(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAP_ADDINFO, [
    ('struFacePicRect', NET_VCA_RECT),
    ('iSwingAngle', c_int),
    ('iTiltAngle', c_int),
    ('dwPupilDistance', DWORD),
    ('byBlockingState', BYTE),
    ('byFaceSnapThermometryEnabled', BYTE),
    ('byIsAbnomalTemperature', BYTE),
    ('byThermometryUnit', BYTE),
    ('struEnterTime', NET_DVR_TIME_EX),
    ('struExitTime', NET_DVR_TIME_EX),
    ('fFaceTemperature', c_float),
    ('fAlarmTemperature', c_float),
    ('dwThermalPicLen', DWORD),
    ('pThermalPicBuff', POINTER(BYTE)),
    ('szCustomChanID', BYTE * 65),
    ('byRes1', BYTE * 3),
    ('struLLPos', NET_DVR_LLPOS_PARAM),
    ('pEventNotificationAlertBuff', String),
    ('dwEventNotificationAlertLen', DWORD),
    ('byRes', BYTE * 340),
])

NET_VCA_FACESNAP_ADDINFO = struct_tagNET_VCA_FACESNAP_ADDINFO
LPNET_VCA_FACESNAP_ADDINFO = POINTER(struct_tagNET_VCA_FACESNAP_ADDINFO)
tagNET_VCA_FACESNAP_ADDINFO = struct_tagNET_VCA_FACESNAP_ADDINFO
