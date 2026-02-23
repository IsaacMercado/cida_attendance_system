from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECORDING_PUBLISH_FILE_COND(Structure):
    pass

_S(struct_tagNET_DVR_RECORDING_PUBLISH_FILE_COND, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byFileID', BYTE * 128),
    ('byRes', BYTE * 300),
])

NET_DVR_RECORDING_PUBLISH_FILE_COND = struct_tagNET_DVR_RECORDING_PUBLISH_FILE_COND
LPNET_DVR_RECORDING_PUBLISH_FILE_COND = POINTER(struct_tagNET_DVR_RECORDING_PUBLISH_FILE_COND)
tagNET_DVR_RECORDING_PUBLISH_FILE_COND = struct_tagNET_DVR_RECORDING_PUBLISH_FILE_COND
