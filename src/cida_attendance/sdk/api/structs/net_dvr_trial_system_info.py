from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_videoin_type_info import NET_DVR_VIDEOIN_TYPE_INFO


class struct_tagNET_DVR_TRIAL_SYSTEM_INFO(Structure):
    pass

_S(struct_tagNET_DVR_TRIAL_SYSTEM_INFO, [
    ('dwSize', DWORD),
    ('byVideoInTypeNum', BYTE),
    ('byRes1', BYTE * 3),
    ('struVideoIn', NET_DVR_VIDEOIN_TYPE_INFO * 10),
    ('byRes', BYTE * 512),
])

NET_DVR_TRIAL_SYSTEM_INFO = struct_tagNET_DVR_TRIAL_SYSTEM_INFO
LPNET_DVR_TRIAL_SYSTEM_INFO = POINTER(struct_tagNET_DVR_TRIAL_SYSTEM_INFO)
tagNET_DVR_TRIAL_SYSTEM_INFO = struct_tagNET_DVR_TRIAL_SYSTEM_INFO
