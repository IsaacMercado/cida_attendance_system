from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RTSP_PROTOCAL_CFG(Structure):
    pass

_S(struct_tagNET_DVR_RTSP_PROTOCAL_CFG, [
    ('byEnable', BYTE),
    ('byLocalBackUp', BYTE),
    ('byRes', BYTE * 2),
    ('strURL', BYTE * 256),
    ('dwProtocalType', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassWord', BYTE * 16),
    ('byAddress', BYTE * 64),
    ('wPort', WORD),
    ('byRes1', BYTE * 122),
])

NET_DVR_RTSP_PROTOCAL_CFG = struct_tagNET_DVR_RTSP_PROTOCAL_CFG
LPNET_DVR_RTSP_PROTOCAL_CFG = POINTER(struct_tagNET_DVR_RTSP_PROTOCAL_CFG)
tagNET_DVR_RTSP_PROTOCAL_CFG = struct_tagNET_DVR_RTSP_PROTOCAL_CFG
