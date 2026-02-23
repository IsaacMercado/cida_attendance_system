from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .anon_333 import union_anon_333


class struct_tagNET_DVR_DECODECHANCFG_SCENE(Structure):
    pass

_S(struct_tagNET_DVR_DECODECHANCFG_SCENE, [
    ('byDecodeEnable', BYTE),
    ('bySlotNum', BYTE),
    ('byDecChan', BYTE),
    ('byRes', BYTE * 5),
    ('struDecCfg', union_anon_333),
])

NET_DVR_DECODECHANCFG_SCENE = struct_tagNET_DVR_DECODECHANCFG_SCENE
LPNET_DVR_DECODECHANCFG_SCENE = POINTER(struct_tagNET_DVR_DECODECHANCFG_SCENE)
tagNET_DVR_DECODECHANCFG_SCENE = struct_tagNET_DVR_DECODECHANCFG_SCENE
