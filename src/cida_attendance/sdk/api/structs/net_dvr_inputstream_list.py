from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_inputstreamcfg import NET_DVR_INPUTSTREAMCFG


class struct_tagNET_DVR_INPUTSTREAM_LIST(Structure):
    pass

_S(struct_tagNET_DVR_INPUTSTREAM_LIST, [
    ('dwSize', DWORD),
    ('struInputStreamInfo', NET_DVR_INPUTSTREAMCFG * 224),
    ('byRes', BYTE * 4),
])

NET_DVR_INPUTSTREAM_LIST = struct_tagNET_DVR_INPUTSTREAM_LIST
LPNET_DVR_INPUTSTREAM_LIST = POINTER(struct_tagNET_DVR_INPUTSTREAM_LIST)
tagNET_DVR_INPUTSTREAM_LIST = struct_tagNET_DVR_INPUTSTREAM_LIST
