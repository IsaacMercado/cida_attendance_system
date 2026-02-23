from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUTVOLUME(Structure):
    pass

_S(struct_tagNET_DVR_INPUTVOLUME, [
    ('dwSize', DWORD),
    ('byAudioInputChan', BYTE),
    ('byRes', BYTE * 63),
])

NET_DVR_INPUTVOLUME = struct_tagNET_DVR_INPUTVOLUME
LPNET_DVR_INPUTVOLUME = POINTER(struct_tagNET_DVR_INPUTVOLUME)
tagNET_DVR_INPUTVOLUME = struct_tagNET_DVR_INPUTVOLUME
