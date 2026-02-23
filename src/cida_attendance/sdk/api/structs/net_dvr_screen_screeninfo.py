from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_screen_union import NET_DVR_SCREEN_UNION


class struct_tagNET_DVR_SCREEN_SCREENINFO(Structure):
    pass

_S(struct_tagNET_DVR_SCREEN_SCREENINFO, [
    ('dwSize', DWORD),
    ('byValid', BYTE),
    ('nLinkMode', BYTE),
    ('byDeviceType', BYTE),
    ('byScreenLayX', BYTE),
    ('byScreenLayY', BYTE),
    ('byRes1', BYTE * 3),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDevName', BYTE * 32),
    ('struScreenUnion', NET_DVR_SCREEN_UNION),
    ('byInputNum', BYTE),
    ('byOutputNum', BYTE),
    ('byCBDNum', BYTE),
    ('byRes2', BYTE * 29),
])

NET_DVR_SCREEN_SCREENINFO = struct_tagNET_DVR_SCREEN_SCREENINFO
LPNET_DVR_SCREEN_SCREENINFO = POINTER(struct_tagNET_DVR_SCREEN_SCREENINFO)
tagNET_DVR_SCREEN_SCREENINFO = struct_tagNET_DVR_SCREEN_SCREENINFO
