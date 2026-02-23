from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_agegroup_param import NET_DVR_AGEGROUP_PARAM
from .net_dvr_program_info import NET_DVR_PROGRAM_INFO
from .net_dvr_sexgroup_param import NET_DVR_SEXGROUP_PARAM
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_FACECAPTURE_STATISTICS_RESULT_(Structure):
    pass

_S(struct_tagNET_DVR_FACECAPTURE_STATISTICS_RESULT_, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byStatType', BYTE),
    ('byRes', BYTE * 7),
    ('dwPeopleNum', DWORD),
    ('struAgeGroupParam', NET_DVR_AGEGROUP_PARAM),
    ('struSexGroupParam', NET_DVR_SEXGROUP_PARAM),
    ('struProgramInfo', NET_DVR_PROGRAM_INFO),
    ('byRes1', BYTE * 76),
])

NET_DVR_FACECAPTURE_STATISTICS_RESULT = struct_tagNET_DVR_FACECAPTURE_STATISTICS_RESULT_
LPNET_DVR_FACECAPTURE_STATISTICS_RESULT = POINTER(struct_tagNET_DVR_FACECAPTURE_STATISTICS_RESULT_)
tagNET_DVR_FACECAPTURE_STATISTICS_RESULT_ = struct_tagNET_DVR_FACECAPTURE_STATISTICS_RESULT_
