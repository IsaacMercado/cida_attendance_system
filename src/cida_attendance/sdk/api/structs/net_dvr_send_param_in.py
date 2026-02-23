from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_time_v30 import NET_DVR_TIME_V30


class struct_tagNET_DVR_SEND_PARAM_IN(Structure):
    pass

_S(struct_tagNET_DVR_SEND_PARAM_IN, [
    ('pSendData', POINTER(BYTE)),
    ('dwSendDataLen', DWORD),
    ('struTime', NET_DVR_TIME_V30),
    ('byPicType', BYTE),
    ('byPicURL', BYTE),
    ('byUploadModeling', BYTE),
    ('byRes1', BYTE),
    ('dwPicMangeNo', DWORD),
    ('sPicName', BYTE * 32),
    ('dwPicDisplayTime', DWORD),
    ('pSendAppendData', POINTER(BYTE)),
    ('dwSendAppendDataLen', DWORD),
    ('byRes', BYTE * 192),
])

NET_DVR_SEND_PARAM_IN = struct_tagNET_DVR_SEND_PARAM_IN
LPNET_DVR_SEND_PARAM_IN = POINTER(struct_tagNET_DVR_SEND_PARAM_IN)
tagNET_DVR_SEND_PARAM_IN = struct_tagNET_DVR_SEND_PARAM_IN
