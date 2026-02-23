from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_dispinfo import NET_DVR_DISPINFO
from .net_dvr_dispwindowmode import NET_DVR_DISPWINDOWMODE
from .net_dvr_screeninfo import NET_DVR_SCREENINFO
from .net_dvr_sdi_info import NET_DVR_SDI_INFO


class struct_tagNET_DVR_MATRIX_ABILITY_V41(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_ABILITY_V41, [
    ('dwSize', DWORD),
    ('byDspNums', BYTE),
    ('byDecChanNums', BYTE),
    ('byStartChan', BYTE),
    ('byRes1', BYTE * 5),
    ('struVgaInfo', NET_DVR_DISPINFO),
    ('struBncInfo', NET_DVR_DISPINFO),
    ('struHdmiInfo', NET_DVR_DISPINFO),
    ('struDviInfo', NET_DVR_DISPINFO),
    ('struDispMode', NET_DVR_DISPWINDOWMODE * 32),
    ('struBigScreenInfo', NET_DVR_SCREENINFO),
    ('bySupportAutoReboot', BYTE),
    ('byRes2', BYTE * 3),
    ('struSDIInfo', NET_DVR_SDI_INFO),
    ('byRes3', BYTE * 48),
])

NET_DVR_MATRIX_ABILITY_V41 = struct_tagNET_DVR_MATRIX_ABILITY_V41
LPNET_DVR_MATRIX_ABILITY_V41 = POINTER(struct_tagNET_DVR_MATRIX_ABILITY_V41)
tagNET_DVR_MATRIX_ABILITY_V41 = struct_tagNET_DVR_MATRIX_ABILITY_V41
