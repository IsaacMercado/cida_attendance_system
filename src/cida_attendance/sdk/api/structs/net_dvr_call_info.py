from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_conference_call_info import NET_DVR_CONFERENCE_CALL_INFO
from .net_dvr_terminal_call_info import NET_DVR_TERMINAL_CALL_INFO


class union_tagNET_DVR_CALL_INFO(Union):
    pass

_S(union_tagNET_DVR_CALL_INFO, [
    ('byRes', BYTE * 640),
    ('struTerminalCallInfo', NET_DVR_TERMINAL_CALL_INFO),
    ('struConferenceCallInfo', NET_DVR_CONFERENCE_CALL_INFO),
])

NET_DVR_CALL_INFO = union_tagNET_DVR_CALL_INFO
LPNET_DVR_CALL_INFO = POINTER(union_tagNET_DVR_CALL_INFO)
tagNET_DVR_CALL_INFO = union_tagNET_DVR_CALL_INFO
