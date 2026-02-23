from ctypes import Structure, c_int

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_AEMODECFG(Structure):
    pass

_S(struct_tagNET_DVR_AEMODECFG, [
    ('dwSize', DWORD),
    ('iIrisSet', c_int),
    ('iGainSet', c_int),
    ('iGainLimit', c_int),
    ('iExposureCompensate', c_int),
    ('byExposureModeSet', BYTE),
    ('byShutterSet', BYTE),
    ('byImageStabilizeLevel', BYTE),
    ('byCameraIrCorrect', BYTE),
    ('byHighSensitivity', BYTE),
    ('byInitializeLens', BYTE),
    ('byChromaSuppress', BYTE),
    ('byMaxShutterSet', BYTE),
    ('byMinShutterSet', BYTE),
    ('byMaxIrisSet', BYTE),
    ('byMinIrisSet', BYTE),
    ('byExposureLevel', BYTE),
    ('byRes', BYTE * 60),
])

NET_DVR_AEMODECFG = struct_tagNET_DVR_AEMODECFG
LPNET_DVR_AEMODECFG = POINTER(struct_tagNET_DVR_AEMODECFG)
tagNET_DVR_AEMODECFG = struct_tagNET_DVR_AEMODECFG
