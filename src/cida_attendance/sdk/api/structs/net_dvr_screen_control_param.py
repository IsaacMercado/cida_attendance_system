from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_area_zoom_cfg import NET_DVR_AREA_ZOOM_CFG
from .net_dvr_display_color_ctrl import NET_DVR_DISPLAY_COLOR_CTRL
from .net_dvr_display_position_ctrl import NET_DVR_DISPLAY_POSITION_CTRL
from .net_dvr_input_interface_ctrl import NET_DVR_INPUT_INTERFACE_CTRL
from .net_dvr_screen_wall_ctrl import NET_DVR_SCREEN_WALL_CTRL
from .net_dvr_simulate_remote_ctrl import NET_DVR_SIMULATE_REMOTE_CTRL


class union_tagNET_DVR_SCREEN_CONTROL_PARAM(Union):
    pass

_S(union_tagNET_DVR_SCREEN_CONTROL_PARAM, [
    ('struInputCtrl', NET_DVR_INPUT_INTERFACE_CTRL),
    ('struDisplayCtrl', NET_DVR_DISPLAY_COLOR_CTRL),
    ('struPositionCtrl', NET_DVR_DISPLAY_POSITION_CTRL),
    ('struSimulateRemoteCrtl', NET_DVR_SIMULATE_REMOTE_CTRL),
    ('struScreenWallCtrl', NET_DVR_SCREEN_WALL_CTRL),
    ('struZoomArea', NET_DVR_AREA_ZOOM_CFG),
    ('byRes', BYTE * 16),
])

NET_DVR_SCREEN_CONTROL_PARAM = union_tagNET_DVR_SCREEN_CONTROL_PARAM
LPNET_DVR_SCREEN_CONTROL_PARAM = POINTER(union_tagNET_DVR_SCREEN_CONTROL_PARAM)
tagNET_DVR_SCREEN_CONTROL_PARAM = union_tagNET_DVR_SCREEN_CONTROL_PARAM
