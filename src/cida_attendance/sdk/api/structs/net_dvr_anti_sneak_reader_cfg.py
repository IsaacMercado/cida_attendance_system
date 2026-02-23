from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_anti_sneak_host_reader_info import NET_DVR_ANTI_SNEAK_HOST_READER_INFO


class struct_tagNET_DVR_ANTI_SNEAK_READER_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ANTI_SNEAK_READER_CFG, [
    ('byEnable', BYTE),
    ('byAntiSnealHostNo', BYTE),
    ('wReaderID', WORD),
    ('struSneakReaderInfo', NET_DVR_ANTI_SNEAK_HOST_READER_INFO * 8),
    ('byRes2', BYTE * 8),
])

NET_DVR_ANTI_SNEAK_READER_CFG = struct_tagNET_DVR_ANTI_SNEAK_READER_CFG
LPNET_DVR_ANTI_SNEAK_READER_CFG = POINTER(struct_tagNET_DVR_ANTI_SNEAK_READER_CFG)
tagNET_DVR_ANTI_SNEAK_READER_CFG = struct_tagNET_DVR_ANTI_SNEAK_READER_CFG
