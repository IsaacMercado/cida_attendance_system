from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIXSWITCHCTRL(Structure):
    pass

_S(struct_tagNET_DVR_MATRIXSWITCHCTRL, [
    ('dwCamId', DWORD),
    ('dwMonId', DWORD),
    ('bySubWindowNum', BYTE),
    ('bySwitchType', BYTE),
    ('wAlarmType', WORD),
    ('dwResidentTime', DWORD),
    ('byVcaDevType', BYTE),
    ('byWallNo', BYTE),
    ('byRes', BYTE * 18),
])

NET_DVR_MATRIXSWITCHCTRL = struct_tagNET_DVR_MATRIXSWITCHCTRL
LPNET_DVR_MATRIXSWITCHCTRL = POINTER(struct_tagNET_DVR_MATRIXSWITCHCTRL)
tagNET_DVR_MATRIXSWITCHCTRL = struct_tagNET_DVR_MATRIXSWITCHCTRL
