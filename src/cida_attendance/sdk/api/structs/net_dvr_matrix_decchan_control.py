from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_MATRIX_DECCHAN_CONTROL(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_DECCHAN_CONTROL, [
    ('dwSize', DWORD),
    ('byDecChanScaleStatus', BYTE),
    ('byDecodeDelay', BYTE),
    ('byEnableSpartan', BYTE),
    ('byLowLight', BYTE),
    ('byNoiseReduction', BYTE),
    ('byDefog', BYTE),
    ('byEnableVcaDec', BYTE),
    ('byEnableAudio', BYTE),
    ('dwAllCtrlType', DWORD),
    ('byVolume', BYTE),
    ('byRes', BYTE * 55),
])

NET_DVR_MATRIX_DECCHAN_CONTROL = struct_tagNET_DVR_MATRIX_DECCHAN_CONTROL
LPNET_DVR_MATRIX_DECCHAN_CONTROL = POINTER(struct_tagNET_DVR_MATRIX_DECCHAN_CONTROL)
tagNET_DVR_MATRIX_DECCHAN_CONTROL = struct_tagNET_DVR_MATRIX_DECCHAN_CONTROL
