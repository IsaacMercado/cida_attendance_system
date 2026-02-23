from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_vca_dev_info import NET_VCA_DEV_INFO


class struct_tagNET_DVR_FRAMES_PEOPLE_COUNTING(Structure):
    pass

_S(struct_tagNET_DVR_FRAMES_PEOPLE_COUNTING, [
    ('dwSize', DWORD),
    ('struDevInfo', NET_VCA_DEV_INFO),
    ('dwRelativeTime', DWORD),
    ('dwAbsTime', DWORD),
    ('dwPeopleCountingNum', DWORD),
    ('dwPicLen', DWORD),
    ('pPicBuffer', POINTER(BYTE)),
    ('byRes', BYTE * 512),
])

NET_DVR_FRAMES_PEOPLE_COUNTING = struct_tagNET_DVR_FRAMES_PEOPLE_COUNTING
LPNET_DVR_FRAMES_PEOPLE_COUNTING = POINTER(struct_tagNET_DVR_FRAMES_PEOPLE_COUNTING)
tagNET_DVR_FRAMES_PEOPLE_COUNTING = struct_tagNET_DVR_FRAMES_PEOPLE_COUNTING
