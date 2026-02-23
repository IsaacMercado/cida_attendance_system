from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_VS_NETSRC_CFG(Structure):
    pass

_S(struct_tagNET_DVR_VS_NETSRC_CFG, [
    ('dwSize', DWORD),
    ('dwVSInputChan', DWORD),
    ('byDispUrl', BYTE * 512),
    ('byEnabled', BYTE),
    ('byRes', BYTE * 127),
])

NET_DVR_VS_NETSRC_CFG = struct_tagNET_DVR_VS_NETSRC_CFG
LPNET_DVR_VS_NETSRC_CFG = POINTER(struct_tagNET_DVR_VS_NETSRC_CFG)
tagNET_DVR_VS_NETSRC_CFG = struct_tagNET_DVR_VS_NETSRC_CFG
