from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_INPUT_SIGNAL_LIST(Structure):
    pass

_S(struct_tagNET_DVR_INPUT_SIGNAL_LIST, [
    ('dwSize', DWORD),
    ('dwInputSignalNums', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('byRes1', BYTE * 3),
    ('dwBufLen', DWORD),
    ('byRes2', BYTE * 64),
])

NET_DVR_INPUT_SIGNAL_LIST = struct_tagNET_DVR_INPUT_SIGNAL_LIST
LPNET_DVR_INPUT_SIGNAL_LIST = POINTER(struct_tagNET_DVR_INPUT_SIGNAL_LIST)
tagNET_DVR_INPUT_SIGNAL_LIST = struct_tagNET_DVR_INPUT_SIGNAL_LIST
