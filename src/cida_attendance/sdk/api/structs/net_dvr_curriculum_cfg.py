from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_each_lesson_info import NET_DVR_EACH_LESSON_INFO


class struct_tagNET_DVR_CURRICULUM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CURRICULUM_CFG, [
    ('dwSize', DWORD),
    ('struLessonInfo', NET_DVR_EACH_LESSON_INFO * 16),
    ('byRes', BYTE * 256),
])

NET_DVR_CURRICULUM_CFG = struct_tagNET_DVR_CURRICULUM_CFG
LPNET_DVR_CURRICULUM_CFG = POINTER(struct_tagNET_DVR_CURRICULUM_CFG)
tagNET_DVR_CURRICULUM_CFG = struct_tagNET_DVR_CURRICULUM_CFG
