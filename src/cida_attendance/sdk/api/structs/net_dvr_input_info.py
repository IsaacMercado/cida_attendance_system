from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_INFO, [
    ('dwSize', DWORD),
    ('byChanType', BYTE),
    ('byRes1', BYTE * 3),
    ('dwChanNo', DWORD),
    ('dwSubChanNo', DWORD),
    ('dwVariableNo', DWORD),
    ('byRemoteType', BYTE),
    ('byLinkageIPCType', BYTE),
    ('byLinkageTriggerType', BYTE),
    ('byRes2', BYTE * 57),
])

NET_DVR_INPUT_INFO = struct_tagNET_DVR_INPUT_INFO
LPNET_DVR_INPUT_INFO = POINTER(struct_tagNET_DVR_INPUT_INFO)
tagNET_DVR_INPUT_INFO = struct_tagNET_DVR_INPUT_INFO
