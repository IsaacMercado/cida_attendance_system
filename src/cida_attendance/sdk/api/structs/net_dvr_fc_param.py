from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FC_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FC_PARAM, [
    ('dwSize', DWORD),
    ('dwStoreLunID', DWORD),
    ('dwLogicLunID', DWORD),
    ('dwHbaID', DWORD),
    ('dwAccessMode', DWORD),
    ('szClientWWWPN', c_char * 32),
    ('byRes', BYTE * 32),
])

NET_DVR_FC_PARAM = struct_tagNET_DVR_FC_PARAM
LPNET_DVR_FC_PARAM = POINTER(struct_tagNET_DVR_FC_PARAM)
tagNET_DVR_FC_PARAM = struct_tagNET_DVR_FC_PARAM
