from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_USER_INFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_USER_INFO_V40, [
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('byLocalRight', BYTE * 32),
    ('byRemoteRight', BYTE * 32),
    ('dwNetPreviewRight', DWORD * 512),
    ('dwLocalRecordRight', DWORD * 512),
    ('dwNetRecordRight', DWORD * 512),
    ('dwLocalPlaybackRight', DWORD * 512),
    ('dwNetPlaybackRight', DWORD * 512),
    ('dwLocalPTZRight', DWORD * 512),
    ('dwNetPTZRight', DWORD * 512),
    ('dwLocalBackupRight', DWORD * 512),
    ('struUserIP', NET_DVR_IPADDR),
    ('byMACAddr', BYTE * 6),
    ('byPriority', BYTE),
    ('byAlarmOnRight', BYTE),
    ('byAlarmOffRight', BYTE),
    ('byBypassRight', BYTE),
    ('byRes1', BYTE * 2),
    ('byPublishRight', BYTE * 32),
    ('byRes', BYTE * 84),
])

NET_DVR_USER_INFO_V40 = struct_tagNET_DVR_USER_INFO_V40
LPNET_DVR_USER_INFO_V40 = POINTER(struct_tagNET_DVR_USER_INFO_V40)
tagNET_DVR_USER_INFO_V40 = struct_tagNET_DVR_USER_INFO_V40
