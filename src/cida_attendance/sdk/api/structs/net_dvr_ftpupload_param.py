from ctypes import Structure, c_char

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FTPUPLOAD_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_FTPUPLOAD_PARAM, [
    ('szRuleTypeItem', c_char * 20),
    ('szCameraName', c_char * 32),
    ('byRes', BYTE * 64),
])

NET_DVR_FTPUPLOAD_PARAM = struct_tagNET_DVR_FTPUPLOAD_PARAM
LPNET_DVR_FTPUPLOAD_PARAM = POINTER(struct_tagNET_DVR_FTPUPLOAD_PARAM)
tagNET_DVR_FTPUPLOAD_PARAM = struct_tagNET_DVR_FTPUPLOAD_PARAM
