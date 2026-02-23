from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AGEGROUP_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_AGEGROUP_PARAM_, [
    ('dwTeenage', DWORD),
    ('dwYouth', DWORD),
    ('dwMidLife', DWORD),
    ('dwElderly', DWORD),
    ('dwChild', DWORD),
    ('dwAdolescent', DWORD),
    ('dwPrime', DWORD),
    ('dwMidage', DWORD),
    ('byRes', BYTE * 48),
])

NET_DVR_AGEGROUP_PARAM = struct_tagNET_DVR_AGEGROUP_PARAM_
LPNET_DVR_AGEGROUP_PARAM = POINTER(struct_tagNET_DVR_AGEGROUP_PARAM_)
tagNET_DVR_AGEGROUP_PARAM_ = struct_tagNET_DVR_AGEGROUP_PARAM_
