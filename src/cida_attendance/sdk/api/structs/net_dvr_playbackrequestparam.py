from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .anon_328 import union_anon_328


class struct_tagNET_DVR_PLAYBACKREQUESTPARAM(Structure):
    pass

_S(struct_tagNET_DVR_PLAYBACKREQUESTPARAM, [
    ('byPlayBackMode', BYTE),
    ('byRes1', BYTE * 3),
    ('playbackmode', union_anon_328),
    ('struCuIp', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('byRes2', BYTE * 2),
    ('dwSessionID', DWORD),
    ('byRes3', BYTE * 16),
])

NET_DVR_PLAYBACKREQUESTPARAM = struct_tagNET_DVR_PLAYBACKREQUESTPARAM
LPNET_DVR_PLAYBACKREQUESTPARAM = POINTER(struct_tagNET_DVR_PLAYBACKREQUESTPARAM)
tagNET_DVR_PLAYBACKREQUESTPARAM = struct_tagNET_DVR_PLAYBACKREQUESTPARAM
