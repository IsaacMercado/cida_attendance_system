from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUTSTREAM_PTZCFG_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_INPUTSTREAM_PTZCFG_PARAM, [
    ('dwSize', DWORD),
    ('wPTZProtocol', WORD),
    ('byRes', BYTE * 34),
])

NET_DVR_INPUTSTREAM_PTZCFG_PARAM = struct_tagNET_DVR_INPUTSTREAM_PTZCFG_PARAM
LPNET_DVR_INPUTSTREAM_PTZCFG_PARAM = POINTER(struct_tagNET_DVR_INPUTSTREAM_PTZCFG_PARAM)
tagNET_DVR_INPUTSTREAM_PTZCFG_PARAM = struct_tagNET_DVR_INPUTSTREAM_PTZCFG_PARAM
