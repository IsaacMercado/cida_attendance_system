from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_TRUNKLIST(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_TRUNKLIST, [
    ('dwSize', DWORD),
    ('byRes', BYTE * 12),
    ('dwTrunkNum', DWORD),
    ('pBuffer', POINTER(BYTE)),
    ('dwBufLen', DWORD),
])

NET_DVR_MATRIX_TRUNKLIST = struct_tagNET_DVR_MATRIX_TRUNKLIST
LPNET_DVR_MATRIX_TRUNKLIST = POINTER(struct_tagNET_DVR_MATRIX_TRUNKLIST)
tagNET_DVR_MATRIX_TRUNKLIST = struct_tagNET_DVR_MATRIX_TRUNKLIST
