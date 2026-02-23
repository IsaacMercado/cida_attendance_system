from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .net_vca_rect import NET_VCA_RECT


class struct_tagNET_DVR_SPRCFG(Structure):
    pass

_S(struct_tagNET_DVR_SPRCFG, [
    ('dwSize', DWORD),
    ('byDefaultCHN', BYTE * 3),
    ('byPlateOSD', BYTE),
    ('bySendJPEG1', BYTE),
    ('bySendJPEG2', BYTE),
    ('wDesignedPlateWidth', WORD),
    ('byTotalLaneNum', BYTE),
    ('byRes1', BYTE),
    ('wRecognizedLane', WORD),
    ('struLaneRect', NET_VCA_RECT * 5),
    ('dwRecogMode', DWORD),
    ('bySendPRRaw', BYTE),
    ('bySendBinImage', BYTE),
    ('byDelayCapture', BYTE),
    ('byUseLED', BYTE),
    ('byRes2', BYTE * 68),
])

NET_DVR_SPRCFG = struct_tagNET_DVR_SPRCFG
LPNET_DVR_SPRCFG = POINTER(struct_tagNET_DVR_SPRCFG)
tagNET_DVR_SPRCFG = struct_tagNET_DVR_SPRCFG
