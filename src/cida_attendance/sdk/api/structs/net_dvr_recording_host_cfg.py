from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORDING_HOST_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RECORDING_HOST_CFG, [
    ('dwSize', DWORD),
    ('dwOneKeyDelayTime', DWORD),
    ('byDirectedMode', BYTE),
    ('byClassroomType', BYTE),
    ('byCourseDataStorageEnabled', BYTE),
    ('byElectronicEnlargeMode', BYTE),
    ('byRes', BYTE * 124),
])

NET_DVR_RECORDING_HOST_CFG = struct_tagNET_DVR_RECORDING_HOST_CFG
LPNET_DVR_RECORDING_HOST_CFG = POINTER(struct_tagNET_DVR_RECORDING_HOST_CFG)
tagNET_DVR_RECORDING_HOST_CFG = struct_tagNET_DVR_RECORDING_HOST_CFG
