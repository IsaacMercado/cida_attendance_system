from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NOISEREMOVE(Structure):
    pass

_S(struct_tagNET_DVR_NOISEREMOVE, [
    ('byDigitalNoiseRemoveEnable', BYTE),
    ('byDigitalNoiseRemoveLevel', BYTE),
    ('bySpectralLevel', BYTE),
    ('byTemporalLevel', BYTE),
    ('byDigitalNoiseRemove2DEnable', BYTE),
    ('byDigitalNoiseRemove2DLevel', BYTE),
    ('byRes', BYTE * 2),
])

NET_DVR_NOISEREMOVE = struct_tagNET_DVR_NOISEREMOVE
LPNET_DVR_NOISEREMOVE = POINTER(struct_tagNET_DVR_NOISEREMOVE)
tagNET_DVR_NOISEREMOVE = struct_tagNET_DVR_NOISEREMOVE
