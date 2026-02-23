from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .anon_304 import NET_DVR_INQUEST_FILEINFO


class struct_anon_305(Structure):
    pass

_S(struct_anon_305, [
    ('dwFileNum', DWORD),
    ('struFileInfo', NET_DVR_INQUEST_FILEINFO * 20),
    ('dwCDIndex', DWORD),
    ('bFinalizeDisc', DWORD),
])

NET_DVR_INQUEST_FILES = struct_anon_305
LPNET_DVR_INQUEST_FILES = POINTER(struct_anon_305)
