from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RESUME_INITRACKPOS_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RESUME_INITRACKPOS_CFG, [
    ('dwSize', DWORD),
    ('dwChannel', DWORD),
    ('byRes', BYTE * 16),
])

NET_DVR_RESUME_INITRACKPOS_CFG = struct_tagNET_DVR_RESUME_INITRACKPOS_CFG
LPNET_DVR_RESUME_INITRACKPOS_CFG = POINTER(struct_tagNET_DVR_RESUME_INITRACKPOS_CFG)
tagNET_DVR_RESUME_INITRACKPOS_CFG = struct_tagNET_DVR_RESUME_INITRACKPOS_CFG
