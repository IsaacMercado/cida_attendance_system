from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SNAPENABLECFG(Structure):
    pass

_S(struct_tagNET_DVR_SNAPENABLECFG, [
    ('dwSize', DWORD),
    ('byPlateEnable', BYTE),
    ('byRes1', BYTE * 2),
    ('byFrameFlip', BYTE),
    ('wFlipAngle', WORD),
    ('wLightPhase', WORD),
    ('byLightSyncPower', BYTE),
    ('byFrequency', BYTE),
    ('byUploadSDEnable', BYTE),
    ('byPlateMode', BYTE),
    ('byUploadInfoFTP', BYTE),
    ('byAutoFormatSD', BYTE),
    ('wJpegPicSize', WORD),
    ('bySnapPicResolution', BYTE),
    ('byRes', BYTE * 55),
])

NET_DVR_SNAPENABLECFG = struct_tagNET_DVR_SNAPENABLECFG
LPNET_DVR_SNAPENABLECFG = POINTER(struct_tagNET_DVR_SNAPENABLECFG)
tagNET_DVR_SNAPENABLECFG = struct_tagNET_DVR_SNAPENABLECFG
