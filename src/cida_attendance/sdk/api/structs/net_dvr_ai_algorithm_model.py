from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String


class struct_tagNET_DVR_AI_ALGORITHM_MODEL(Structure):
    pass

_S(struct_tagNET_DVR_AI_ALGORITHM_MODEL, [
    ('dwSize', DWORD),
    ('dwDescribeLength', DWORD),
    ('pDescribeBuffer', String),
    ('byRes1', BYTE * 3),
    ('dwLicenseKeyLength', DWORD),
    ('pLicenseKeyBuffer', String),
    ('byRes', BYTE * 120),
])

NET_DVR_AI_ALGORITHM_MODEL = struct_tagNET_DVR_AI_ALGORITHM_MODEL
LPNET_DVR_AI_ALGORITHM_MODEL = POINTER(struct_tagNET_DVR_AI_ALGORITHM_MODEL)
tagNET_DVR_AI_ALGORITHM_MODEL = struct_tagNET_DVR_AI_ALGORITHM_MODEL
