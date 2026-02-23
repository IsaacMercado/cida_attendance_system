from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_TALK_MODE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_TALK_MODE_CFG, [
    ('byTalkMode', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_LOCAL_TALK_MODE_CFG = struct_tagNET_DVR_LOCAL_TALK_MODE_CFG
LPNET_DVR_LOCAL_TALK_MODE_CFG = POINTER(struct_tagNET_DVR_LOCAL_TALK_MODE_CFG)
tagNET_DVR_LOCAL_TALK_MODE_CFG = struct_tagNET_DVR_LOCAL_TALK_MODE_CFG
