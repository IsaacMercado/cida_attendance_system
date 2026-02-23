from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_mb_ehomepara import NET_DVR_MB_EHOMEPARA
from .net_dvr_mb_wvspara import NET_DVR_MB_WVSPARA


class struct_tagNET_DVR_MB_PLATFORMPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_PLATFORMPARA, [
    ('dwSize', DWORD),
    ('byNetEnvironment', BYTE),
    ('byCurPlatForm', BYTE),
    ('byRes1', BYTE * 2),
    ('struWVSPara', NET_DVR_MB_WVSPARA),
    ('struMbEHpara', NET_DVR_MB_EHOMEPARA),
    ('byRes2', BYTE * 64),
])

NET_DVR_MB_PLATFORMPARA = struct_tagNET_DVR_MB_PLATFORMPARA
LPNET_DVR_MB_PLATFORMPARA = POINTER(struct_tagNET_DVR_MB_PLATFORMPARA)
tagNET_DVR_MB_PLATFORMPARA = struct_tagNET_DVR_MB_PLATFORMPARA
