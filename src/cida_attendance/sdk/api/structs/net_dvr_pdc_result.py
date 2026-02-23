from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_program_info import NET_DVR_PROGRAM_INFO
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_PDC_RESULT(Structure):
    pass

_S(struct_tagNET_DVR_PDC_RESULT, [
    ('dwSize', DWORD),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('dwEnterNum', DWORD),
    ('dwLeaveNum', DWORD),
    ('struProgramInfo', NET_DVR_PROGRAM_INFO),
    ('dwPeoplePassing', DWORD),
    ('byRes1', BYTE * 8),
    ('byISO8601', BYTE),
    ('cStartTimeDifferenceH', c_char),
    ('cStartTimeDifferenceM', c_char),
    ('cStopTimeDifferenceH', c_char),
    ('cStopTimeDifferenceM', c_char),
    ('byRes3', BYTE * 3),
    ('dwDuplicatePeople', DWORD),
    ('dwExpressionUnknown', DWORD),
    ('dwPokerFace', DWORD),
    ('dwHappy', DWORD),
    ('dwSurprised', DWORD),
    ('dwDisgusted', DWORD),
    ('dwSad', DWORD),
    ('dwAngry', DWORD),
    ('dwContemptuous', DWORD),
    ('dwPanic', DWORD),
    ('dwGenderUnknown', DWORD),
    ('dwFemale', DWORD),
    ('dwMale', DWORD),
    ('dwMaskUnknown', DWORD),
    ('dwMaskYes', DWORD),
    ('dwMaskNo', DWORD),
    ('dwGlassUnknown', DWORD),
    ('dwGlassYes', DWORD),
    ('dwGlassNo', DWORD),
    ('dwSunglasses', DWORD),
    ('dwAgeGroupUnknown', DWORD),
    ('dwChild', DWORD),
    ('dwYoung', DWORD),
    ('dwMiddle', DWORD),
    ('dwOld', DWORD),
    ('dwInfant', DWORD),
    ('dwKid', DWORD),
    ('dwTeenager', DWORD),
    ('dwPrime', DWORD),
    ('dwMiddleAged', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_PDC_RESULT = struct_tagNET_DVR_PDC_RESULT
LPNET_DVR_PDC_RESULT = POINTER(struct_tagNET_DVR_PDC_RESULT)
tagNET_DVR_PDC_RESULT = struct_tagNET_DVR_PDC_RESULT
