from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .anon_297 import NET_DVR_PICTURE_NAME
from .anon_299 import NET_DVR_SERIAL_CATCHPIC_PARA


class struct_anon_300(Structure):
    pass

_S(struct_anon_300, [
    ('dwSize', DWORD),
    ('struJpegPara', NET_DVR_JPEGPARA * int((32 + 32))),
    ('wBurstMode', WORD),
    ('wUploadInterval', WORD),
    ('struPicNameRule', NET_DVR_PICTURE_NAME),
    ('bySaveToHD', BYTE),
    ('byRes1', BYTE),
    ('wCatchInterval', WORD),
    ('byRes2', BYTE * 12),
    ('struRs232Cfg', NET_DVR_SERIAL_CATCHPIC_PARA),
    ('struRs485Cfg', NET_DVR_SERIAL_CATCHPIC_PARA),
    ('dwTriggerPicTimes', DWORD * int((32 + 32))),
    ('dwAlarmInPicChanTriggered', DWORD * int((32 + 128))),
])

NET_DVR_JPEGCFG_V30 = struct_anon_300
LPNET_DVR_JPEGCFG_V30 = POINTER(struct_anon_300)
