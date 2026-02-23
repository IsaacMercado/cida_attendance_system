from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FLOW_INFO(Structure):
    pass

_S(struct_tagNET_DVR_FLOW_INFO, [
    ('dwSize', DWORD),
    ('dwSendFlowSize', DWORD),
    ('dwRecvFlowSize', DWORD),
    ('byRes', BYTE * 20),
])

NET_DVR_FLOW_INFO = struct_tagNET_DVR_FLOW_INFO
LPNET_DVR_FLOW_INFO = POINTER(struct_tagNET_DVR_FLOW_INFO)
tagNET_DVR_FLOW_INFO = struct_tagNET_DVR_FLOW_INFO
