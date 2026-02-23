from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_mb_ipaddr import NET_DVR_MB_IPADDR


class struct_tagNET_DVR_MB_EHOMEPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_EHOMEPARA, [
    ('struEHomeAddr', NET_DVR_MB_IPADDR),
    ('byPuid', BYTE * 32),
])

NET_DVR_MB_EHOMEPARA = struct_tagNET_DVR_MB_EHOMEPARA
LPNET_DVR_MB_EHOMEPARA = POINTER(struct_tagNET_DVR_MB_EHOMEPARA)
tagNET_DVR_MB_EHOMEPARA = struct_tagNET_DVR_MB_EHOMEPARA
