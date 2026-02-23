from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ISCSI_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ISCSI_PARAM, [
    ('dwSize', DWORD),
    ('dwTargetID', DWORD),
    ('dwLunID', DWORD),
    ('dwAccessMode', DWORD),
    ('struClientIP', NET_DVR_IPADDR),
    ('byRes', BYTE * 32),
])

NET_DVR_ISCSI_PARAM = struct_tagNET_DVR_ISCSI_PARAM
LPNET_DVR_ISCSI_PARAM = POINTER(struct_tagNET_DVR_ISCSI_PARAM)
tagNET_DVR_ISCSI_PARAM = struct_tagNET_DVR_ISCSI_PARAM
