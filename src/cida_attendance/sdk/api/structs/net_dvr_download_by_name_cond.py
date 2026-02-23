from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER, String
from .net_dvr_address import NET_DVR_ADDRESS


class struct_tagNET_DVR_DOWNLOAD_BY_NAME_COND(Structure):
    pass

_S(struct_tagNET_DVR_DOWNLOAD_BY_NAME_COND, [
    ('pFileName', String),
    ('pSavedFileName', String),
    ('struAddr', NET_DVR_ADDRESS),
    ('byRes', BYTE * 256),
])

NET_DVR_DOWNLOAD_BY_NAME_COND = struct_tagNET_DVR_DOWNLOAD_BY_NAME_COND
LPNET_DVR_DOWNLOAD_BY_NAME_COND = POINTER(struct_tagNET_DVR_DOWNLOAD_BY_NAME_COND)
tagNET_DVR_DOWNLOAD_BY_NAME_COND = struct_tagNET_DVR_DOWNLOAD_BY_NAME_COND
