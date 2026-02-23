from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_advance_screen_check_param import NET_DVR_ADVANCE_SCREEN_CHECK_PARAM
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_SDK_LED_SCREEN_CHECK_PARAM(Structure):
    pass

_S(struct_tagNET_SDK_LED_SCREEN_CHECK_PARAM, [
    ('dwSize', DWORD),
    ('byOperateType', BYTE),
    ('byIsRGBSynChk', BYTE),
    ('byScreenCheckType', BYTE),
    ('byRes1', BYTE),
    ('wRgbPermil', WORD),
    ('wRedPermil', WORD),
    ('wGreenPermil', WORD),
    ('wBluePermil', WORD),
    ('dwRectCount', DWORD),
    ('struRectList', NET_DVR_RECTCFG_EX * 128),
    ('struAdvanceScreenCheckParam', NET_DVR_ADVANCE_SCREEN_CHECK_PARAM),
    ('byRes2', BYTE * 48),
])

NET_SDK_LED_SCREEN_CHECK_PARAM = struct_tagNET_SDK_LED_SCREEN_CHECK_PARAM
LPNET_SDK_LED_SCREEN_CHECK_PARAM = POINTER(struct_tagNET_SDK_LED_SCREEN_CHECK_PARAM)
tagNET_SDK_LED_SCREEN_CHECK_PARAM = struct_tagNET_SDK_LED_SCREEN_CHECK_PARAM
