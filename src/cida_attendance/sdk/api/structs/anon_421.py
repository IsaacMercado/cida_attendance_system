from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_pos_connectmode_union import NET_DVR_POS_CONNECTMODE_UNION


class struct_anon_421(Structure):
    pass

_S(struct_anon_421, [
    ('dwSize', DWORD),
    ('byConnectMode', BYTE),
    ('byRes1', BYTE * 3),
    ('uPosConnMode', NET_DVR_POS_CONNECTMODE_UNION),
    ('byRes', BYTE * 64),
])

NET_DVR_CONNECT_POS_CFG = struct_anon_421
LPNET_DVR_CONNECT_POS_CFG = POINTER(struct_anon_421)
