from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_keyboard_parm import NET_DVR_KEYBOARD_PARAM
from .net_dvr_mark_param import NET_DVR_MARK_PARAM
from .net_dvr_media_list_param import NET_DVR_MEDIA_LIST_PARAM
from .net_dvr_mouse_param import NET_DVR_MOUSE_PARAM
from .net_dvr_ppt_param import NET_DVR_PPT_PARAM
from .net_dvr_remote_ctrl_param import NET_DVR_REMOTE_CTRL_PARAM
from .net_dvr_spotlight_param import NET_DVR_SPOTLIGHT_PARAM
from .net_dvr_touchpad_param import NET_DVR_TOUCHPAD_PARAM


class union_tagNET_DVR_SCREEN_CTRL_PARAM(Union):
    pass

_S(union_tagNET_DVR_SCREEN_CTRL_PARAM, [
    ('struMouseParam', NET_DVR_MOUSE_PARAM),
    ('struMarkParam', NET_DVR_MARK_PARAM),
    ('struKeyboardInfo', NET_DVR_KEYBOARD_PARAM),
    ('struPPTParam', NET_DVR_PPT_PARAM),
    ('struRemoteCtrlParam', NET_DVR_REMOTE_CTRL_PARAM),
    ('struSpotLight', NET_DVR_SPOTLIGHT_PARAM),
    ('struTouchPadParam', NET_DVR_TOUCHPAD_PARAM),
    ('struMediaListParam', NET_DVR_MEDIA_LIST_PARAM),
    ('byRes', BYTE * 16),
])

NET_DVR_SCREEN_CTRL_PARAM = union_tagNET_DVR_SCREEN_CTRL_PARAM
LPNET_DVR_SCREEN_CTRL_PARAM = POINTER(union_tagNET_DVR_SCREEN_CTRL_PARAM)
tagNET_DVR_SCREEN_CTRL_PARAM = union_tagNET_DVR_SCREEN_CTRL_PARAM
