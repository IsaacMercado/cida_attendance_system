from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_174 import union_anon_174
from .anon_175 import union_anon_175
from .net_dvr_pu_stream_url import NET_DVR_PU_STREAM_URL


class struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50, [
    ('dwSize', DWORD),
    ('dwDecChannel', DWORD),
    ('byAddressType', BYTE),
    ('byChannelType', BYTE),
    ('byStreamEncrypt', BYTE),
    ('byRes1', BYTE * 1),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('dwChannel', DWORD),
    ('byStreamId', BYTE * 32),
    ('dwPlayMode', DWORD),
    ('unionAddr', union_anon_174),
    ('unionPlayBackInfo', union_anon_175),
    ('struURL', NET_DVR_PU_STREAM_URL),
    ('sStreamPassword', BYTE * 12),
    ('byRes2', BYTE * 116),
])

NET_DVR_MATRIX_DEC_REMOTE_PLAY_V50 = struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50
LPNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50 = POINTER(struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50)
tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50 = struct_tagNET_DVR_MATRIX_DEC_REMOTE_PLAY_V50
