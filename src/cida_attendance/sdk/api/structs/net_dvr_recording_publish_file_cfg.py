from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_RECORDING_PUBLISH_FILE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RECORDING_PUBLISH_FILE_CFG, [
    ('dwSize', DWORD),
    ('byFileID', BYTE * 128),
    ('struStartTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('byCmdType', BYTE),
    ('byFileType', BYTE),
    ('byRes', BYTE * 254),
])

NET_DVR_RECORDING_PUBLISH_FILE_CFG = struct_tagNET_DVR_RECORDING_PUBLISH_FILE_CFG
LPNET_DVR_RECORDING_PUBLISH_FILE_CFG = POINTER(struct_tagNET_DVR_RECORDING_PUBLISH_FILE_CFG)
tagNET_DVR_RECORDING_PUBLISH_FILE_CFG = struct_tagNET_DVR_RECORDING_PUBLISH_FILE_CFG
