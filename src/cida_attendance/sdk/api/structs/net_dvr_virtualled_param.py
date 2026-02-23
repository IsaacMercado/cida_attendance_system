from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_27 import NET_DVR_RGB_COLOR
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_VIRTUALLED_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_VIRTUALLED_PARAM, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byDispMode', BYTE),
    ('byWndOperateMode', BYTE),
    ('byType', BYTE),
    ('byDirection', BYTE),
    ('byTimeType', BYTE),
    ('byDateFormat', BYTE),
    ('byTimeFormat', BYTE),
    ('struContentColor', NET_DVR_RGB_COLOR),
    ('struBackColor', NET_DVR_RGB_COLOR),
    ('struRect', NET_DVR_RECTCFG_EX),
    ('dwContentNum', DWORD),
    ('byLedContent', BYTE * 512),
    ('byMoveMode', BYTE),
    ('byFontSize', BYTE),
    ('byMoveDirection', BYTE),
    ('byMoveSpeed', BYTE),
    ('struResolution', NET_DVR_RECTCFG_EX),
    ('dwXCoordinate', DWORD),
    ('dwYCoordinate', DWORD),
    ('byHourFormat', BYTE),
    ('byAMFormat', BYTE),
    ('byPMFormat', BYTE),
    ('byAlignmentX', BYTE),
    ('byAlignmentY', BYTE),
    ('byFontType', BYTE),
    ('byRes2', BYTE * 90),
])

NET_DVR_VIRTUALLED_PARAM = struct_tagNET_DVR_VIRTUALLED_PARAM
LPNET_DVR_VIRTUALLED_PARAM = POINTER(struct_tagNET_DVR_VIRTUALLED_PARAM)
tagNET_DVR_VIRTUALLED_PARAM = struct_tagNET_DVR_VIRTUALLED_PARAM
