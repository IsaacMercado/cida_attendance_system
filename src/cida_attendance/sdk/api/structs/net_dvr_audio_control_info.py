from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AUDIO_CONTROL_INFO(Structure):
    pass

_S(struct_tagNET_DVR_AUDIO_CONTROL_INFO, [
    ('dwSize', DWORD),
    ('dwMonId', DWORD),
    ('bySubWindowNum', BYTE),
    ('byWallNo', BYTE),
    ('byEnable', BYTE),
    ('byRes', BYTE * 13),
])

NET_DVR_AUDIO_CONTROL_INFO = struct_tagNET_DVR_AUDIO_CONTROL_INFO
LPNET_DVR_AUDIO_CONTROL_INFO = POINTER(struct_tagNET_DVR_AUDIO_CONTROL_INFO)
tagNET_DVR_AUDIO_CONTROL_INFO = struct_tagNET_DVR_AUDIO_CONTROL_INFO
