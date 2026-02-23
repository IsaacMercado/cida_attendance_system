from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_anon_100(Structure):
    pass

_S(struct_anon_100, [
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byLocalRight', BYTE * 32),
    ('byRemoteRight', BYTE * 32),
    ('byNetPreviewRight', BYTE * int((32 + 32))),
    ('byLocalPlaybackRight', BYTE * int((32 + 32))),
    ('byNetPlaybackRight', BYTE * int((32 + 32))),
    ('byLocalRecordRight', BYTE * int((32 + 32))),
    ('byNetRecordRight', BYTE * int((32 + 32))),
    ('byLocalPTZRight', BYTE * int((32 + 32))),
    ('byNetPTZRight', BYTE * int((32 + 32))),
    ('byLocalBackupRight', BYTE * int((32 + 32))),
    ('struUserIP', NET_DVR_IPADDR),
    ('byMACAddr', BYTE * 6),
    ('byPriority', BYTE),
    ('byAlarmOnRight', BYTE),
    ('byAlarmOffRight', BYTE),
    ('byBypassRight', BYTE),
    ('byRes', BYTE * 14),
])

NET_DVR_USER_INFO_V30 = struct_anon_100
LPNET_DVR_USER_INFO_V30 = POINTER(struct_anon_100)
