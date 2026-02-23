from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_file_response_param import NET_DVR_FILE_RESPONSE_PARAM
from .net_dvr_ppt_response_param import NET_DVR_PPT_RESPONSE_PARAM


class union_tagNET_DVR_SCREEN_RESPONSE_PARAM(Union):
    pass

_S(union_tagNET_DVR_SCREEN_RESPONSE_PARAM, [
    ('byRes', BYTE * 32),
    ('struPPTParam', NET_DVR_PPT_RESPONSE_PARAM),
    ('struFileParam', NET_DVR_FILE_RESPONSE_PARAM),
])

NET_DVR_SCREEN_RESPONSE_PARAM = union_tagNET_DVR_SCREEN_RESPONSE_PARAM
LPNET_DVR_SCREEN_RESPONSE_PARAM = POINTER(union_tagNET_DVR_SCREEN_RESPONSE_PARAM)
tagNET_DVR_SCREEN_RESPONSE_PARAM = union_tagNET_DVR_SCREEN_RESPONSE_PARAM
