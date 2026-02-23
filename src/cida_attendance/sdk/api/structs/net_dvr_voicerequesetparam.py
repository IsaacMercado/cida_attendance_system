from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_VOICEREQUESETPARAM(Structure):
    pass

_S(struct_tagNET_DVR_VOICEREQUESETPARAM, [
    ('nVoiceChannel', BYTE),
    ('byRes1', BYTE * 3),
    ('struCuIp', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes2', BYTE * 10),
])

NET_DVR_VOICEREQUESTPARAM = struct_tagNET_DVR_VOICEREQUESETPARAM
LPNET_DVR_VOICEREQUESTPARAM = POINTER(struct_tagNET_DVR_VOICEREQUESETPARAM)
tagNET_DVR_VOICEREQUESETPARAM = struct_tagNET_DVR_VOICEREQUESETPARAM
