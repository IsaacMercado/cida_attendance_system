from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_VALID_PERIOD_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VALID_PERIOD_CFG, [
    ('byEnable', BYTE),
    ('byBeginTimeFlag', BYTE),
    ('byEnableTimeFlag', BYTE),
    ('byTimeDurationNo', BYTE),
    ('struBeginTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byTimeType', BYTE),
    ('byRes2', BYTE * 31),
])

NET_DVR_VALID_PERIOD_CFG = struct_tagNET_DVR_VALID_PERIOD_CFG
LPNET_DVR_VALID_PERIOD_CFG = POINTER(struct_tagNET_DVR_VALID_PERIOD_CFG)
tagNET_DVR_VALID_PERIOD_CFG = struct_tagNET_DVR_VALID_PERIOD_CFG
