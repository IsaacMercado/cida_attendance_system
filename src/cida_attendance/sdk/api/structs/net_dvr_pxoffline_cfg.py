from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PXOFFLINE_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PXOFFLINE_CFG, [
    ('dwSize', DWORD),
    ('byEnabled', BYTE),
    ('byChargeEnabled', BYTE),
    ('byAlarmEnabled', BYTE),
    ('byRecordSource', BYTE),
    ('dwTimeWait', DWORD),
    ('dwRealeaseMode', DWORD),
    ('byVehCardmatch', BYTE),
    ('bySingleInSingleOut', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_PXOFFLINE_CFG = struct_tagNET_DVR_PXOFFLINE_CFG
LPNET_DVR_PXOFFLINE_CFG = POINTER(struct_tagNET_DVR_PXOFFLINE_CFG)
tagNET_DVR_PXOFFLINE_CFG = struct_tagNET_DVR_PXOFFLINE_CFG
