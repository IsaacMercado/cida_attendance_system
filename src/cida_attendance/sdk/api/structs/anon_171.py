from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_anon_171(Structure):
    pass

_S(struct_anon_171, [
    ('dwSize', DWORD),
    ('dwCurMediaFileLen', DWORD),
    ('dwCurMediaFilePosition', DWORD),
    ('dwCurMediaFileDuration', DWORD),
    ('dwCurPlayTime', DWORD),
    ('dwCurMediaFIleFrames', DWORD),
    ('dwCurDataType', DWORD),
    ('res', BYTE * 72),
])

NET_DVR_MATRIX_DEC_REMOTE_PLAY_STATUS = struct_anon_171
LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_STATUS = POINTER(struct_anon_171)
