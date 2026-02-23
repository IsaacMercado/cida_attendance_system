from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_COMPLETE_RESTORE_INFO_(Structure):
    pass

_S(struct_tagNET_DVR_COMPLETE_RESTORE_INFO_, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 64),
])

NET_DVR_COMPLETE_RESTORE_INFO = struct_tagNET_DVR_COMPLETE_RESTORE_INFO_
LPNET_DVR_COMPLETE_RESTORE_INFO = POINTER(struct_tagNET_DVR_COMPLETE_RESTORE_INFO_)
tagNET_DVR_COMPLETE_RESTORE_INFO_ = struct_tagNET_DVR_COMPLETE_RESTORE_INFO_
