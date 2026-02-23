from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_mb_autoworkpara import NET_DVR_MB_AUTOWORKPARA


class struct_tagNET_DVR_MB_POWERCTRLPARA(Structure):
    pass

_S(struct_tagNET_DVR_MB_POWERCTRLPARA, [
    ('dwSize', DWORD),
    ('dwHaltDelay', DWORD),
    ('struAutoWorkPara', NET_DVR_MB_AUTOWORKPARA),
    ('byEnableUnderVoltProtect', BYTE),
    ('byUnderVoltPercent', BYTE),
    ('byRes', BYTE * 34),
])

NET_DVR_MB_POWERCTRLPARA = struct_tagNET_DVR_MB_POWERCTRLPARA
LPNET_DVR_MB_POWERCTRLPARA = POINTER(struct_tagNET_DVR_MB_POWERCTRLPARA)
tagNET_DVR_MB_POWERCTRLPARA = struct_tagNET_DVR_MB_POWERCTRLPARA
