from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER


class struct_anon_31(Structure):
    pass

_S(struct_anon_31, [
    ('byStreamType', BYTE),
    ('byResolution', BYTE),
    ('byBitrateType', BYTE),
    ('byPicQuality', BYTE),
    ('dwVideoBitrate', DWORD),
    ('dwVideoFrameRate', DWORD),
    ('wIntervalFrameI', WORD),
    ('byIntervalBPFrame', BYTE),
    ('byres1', BYTE),
    ('byVideoEncType', BYTE),
    ('byAudioEncType', BYTE),
    ('byVideoEncComplexity', BYTE),
    ('byEnableSvc', BYTE),
    ('byFormatType', BYTE),
    ('byAudioBitRate', BYTE),
    ('byStreamSmooth', BYTE),
    ('byAudioSamplingRate', BYTE),
    ('bySmartCodec', BYTE),
    ('byDepthMapEnable', BYTE),
    ('wAverageVideoBitrate', WORD),
])

NET_DVR_COMPRESSION_INFO_V30 = struct_anon_31
LPNET_DVR_COMPRESSION_INFO_V30 = POINTER(struct_anon_31)
