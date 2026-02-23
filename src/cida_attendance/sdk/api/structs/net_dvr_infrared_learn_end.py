from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INFRARED_LEARN_END(Structure):
    pass

_S(struct_tagNET_DVR_INFRARED_LEARN_END, [
    ('dwSize', DWORD),
    ('bySaveLearnInfo', BYTE),
    ('byRes', BYTE * 255),
])

NET_DVR_INFRARED_LEARN_END = struct_tagNET_DVR_INFRARED_LEARN_END
LPNET_DVR_INFRARED_LEARN_END = POINTER(struct_tagNET_DVR_INFRARED_LEARN_END)
tagNET_DVR_INFRARED_LEARN_END = struct_tagNET_DVR_INFRARED_LEARN_END
