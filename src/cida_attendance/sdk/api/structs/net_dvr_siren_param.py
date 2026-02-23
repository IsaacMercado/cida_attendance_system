from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SIREN_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_SIREN_PARAM, [
    ('dwSize', DWORD),
    ('byName', BYTE * 32),
    ('wDelay', WORD),
    ('dwOverallEventJointSirenOn', DWORD),
    ('dwSubsystemEventJointSirenOn', DWORD * 32),
    ('byRes2', BYTE * 448),
])

NET_DVR_SIREN_PARAM = struct_tagNET_DVR_SIREN_PARAM
LPNET_DVR_SIREN_PARAM = POINTER(struct_tagNET_DVR_SIREN_PARAM)
tagNET_DVR_SIREN_PARAM = struct_tagNET_DVR_SIREN_PARAM
