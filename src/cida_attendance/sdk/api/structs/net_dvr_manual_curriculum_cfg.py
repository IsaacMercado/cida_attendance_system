from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MANUAL_CURRICULUM_CFG(Structure):
    pass

_S(struct_tagNET_DVR_MANUAL_CURRICULUM_CFG, [
    ('dwSize', DWORD),
    ('byRecUUID', BYTE * 64),
    ('byCourseName', BYTE * 128),
    ('byInstructorName', BYTE * 64),
    ('byCourseDescription', BYTE * 256),
    ('byCmdType', BYTE),
    ('byRes', BYTE * 303),
])

NET_DVR_MANUAL_CURRICULUM_CFG = struct_tagNET_DVR_MANUAL_CURRICULUM_CFG
LPNET_DVR_MANUAL_CURRICULUM_CFG = POINTER(struct_tagNET_DVR_MANUAL_CURRICULUM_CFG)
tagNET_DVR_MANUAL_CURRICULUM_CFG = struct_tagNET_DVR_MANUAL_CURRICULUM_CFG
