from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER, String
from .net_dvr_address import NET_DVR_ADDRESS


class struct_tagNET_DVR_PIC_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_PIC_PARAM, [
    ('pDVRFileName', String),
    ('pSavedFileBuf', String),
    ('dwBufLen', DWORD),
    ('lpdwRetLen', POINTER(DWORD)),
    ('struAddr', NET_DVR_ADDRESS),
    ('byRes', BYTE * 256),
])

NET_DVR_PIC_PARAM = struct_tagNET_DVR_PIC_PARAM
LPNET_DVR_PIC_PARAM = POINTER(struct_tagNET_DVR_PIC_PARAM)
tagNET_DVR_PIC_PARAM = struct_tagNET_DVR_PIC_PARAM
