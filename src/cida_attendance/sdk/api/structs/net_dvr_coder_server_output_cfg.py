from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CODER_SERVER_OUTPUT_CFG(Structure):
    pass

_S(struct_tagNET_DVR_CODER_SERVER_OUTPUT_CFG, [
    ('dwSize', DWORD),
    ('byDispChanType', BYTE),
    ('byVedioFormat', BYTE),
    ('byRes1', BYTE * 2),
    ('dwResolution', DWORD),
    ('dwWindowMode', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_CODER_SERVER_OUTPUT_CFG = struct_tagNET_DVR_CODER_SERVER_OUTPUT_CFG
LPNET_DVR_CODER_SERVER_OUTPUT_CFG = POINTER(struct_tagNET_DVR_CODER_SERVER_OUTPUT_CFG)
tagNET_DVR_CODER_SERVER_OUTPUT_CFG = struct_tagNET_DVR_CODER_SERVER_OUTPUT_CFG
