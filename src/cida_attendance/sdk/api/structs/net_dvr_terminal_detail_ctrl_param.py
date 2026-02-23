from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_terminal_audio_ctrl import NET_DVR_TERMINAL_AUDIO_CTRL
from .net_dvr_terminal_call_info import NET_DVR_TERMINAL_CALL_INFO
from .net_dvr_terminal_input_audio import NET_DVR_TERMINAL_INPUT_AUDIO


class union_tagNET_DVR_TERMINAL_DETAIL_CTRL_PARAM(Union):
    pass

_S(union_tagNET_DVR_TERMINAL_DETAIL_CTRL_PARAM, [
    ('byRes', BYTE * 640),
    ('struCallInfo', NET_DVR_TERMINAL_CALL_INFO),
    ('struAudioCtrl', NET_DVR_TERMINAL_AUDIO_CTRL),
    ('struInputAudio', NET_DVR_TERMINAL_INPUT_AUDIO),
])

NET_DVR_TERMINAL_DETAIL_CTRL_PARAM = union_tagNET_DVR_TERMINAL_DETAIL_CTRL_PARAM
LPNET_DVR_TERMINAL_DETAIL_CTRL_PARAM = POINTER(union_tagNET_DVR_TERMINAL_DETAIL_CTRL_PARAM)
tagNET_DVR_TERMINAL_DETAIL_CTRL_PARAM = union_tagNET_DVR_TERMINAL_DETAIL_CTRL_PARAM
