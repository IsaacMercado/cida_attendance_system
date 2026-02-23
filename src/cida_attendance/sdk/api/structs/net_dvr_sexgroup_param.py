from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SEXGROUP_PARAM_(Structure):
    pass

_S(struct_tagNET_DVR_SEXGROUP_PARAM_, [
    ('dwMale', DWORD),
    ('dwFemale', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_SEXGROUP_PARAM = struct_tagNET_DVR_SEXGROUP_PARAM_
LPNET_DVR_SEXGROUP_PARAM = POINTER(struct_tagNET_DVR_SEXGROUP_PARAM_)
tagNET_DVR_SEXGROUP_PARAM_ = struct_tagNET_DVR_SEXGROUP_PARAM_
