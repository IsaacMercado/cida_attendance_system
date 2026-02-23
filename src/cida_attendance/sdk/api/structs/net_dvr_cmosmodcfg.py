from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_CMOSMODCFG(Structure):
    pass

_S(struct_tagNET_DVR_CMOSMODCFG, [
    ('byCaptureMod', BYTE),
    ('byBrightnessGate', BYTE),
    ('byCaptureGain1', BYTE),
    ('byCaptureGain2', BYTE),
    ('dwCaptureShutterSpeed1', DWORD),
    ('dwCaptureShutterSpeed2', DWORD),
    ('byRes', BYTE * 4),
])

NET_DVR_CMOSMODECFG = struct_tagNET_DVR_CMOSMODCFG
LPNET_DVR_CMOSMODECFG = POINTER(struct_tagNET_DVR_CMOSMODCFG)
tagNET_DVR_CMOSMODCFG = struct_tagNET_DVR_CMOSMODCFG
