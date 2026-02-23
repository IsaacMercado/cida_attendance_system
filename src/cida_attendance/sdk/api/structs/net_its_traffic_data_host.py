from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_ITS_TRAFFIC_DATA_HOST(Structure):
    pass

_S(struct_tagNET_ITS_TRAFFIC_DATA_HOST, [
    ('struHostAddr', NET_DVR_IPADDR),
    ('wHostPort', WORD),
    ('byRes1', BYTE * 2),
    ('dwDataType', DWORD),
    ('bySuspendUpload', BYTE),
    ('byUploadStrategy', BYTE),
    ('wUploadInterval', WORD),
    ('dwUploadTimeOut', DWORD),
    ('byRes', BYTE * 24),
])

NET_ITS_TRAFFIC_DATA_HOST = struct_tagNET_ITS_TRAFFIC_DATA_HOST
LPNET_ITS_TRAFFIC_DATA_HOST = POINTER(struct_tagNET_ITS_TRAFFIC_DATA_HOST)
tagNET_ITS_TRAFFIC_DATA_HOST = struct_tagNET_ITS_TRAFFIC_DATA_HOST
