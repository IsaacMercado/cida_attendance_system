from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .net_dvr_cyc_sur_chan_ele_scene import NET_DVR_CYC_SUR_CHAN_ELE_SCENE


class struct_tagNET_DVR_MATRIX_LOOP_DECINFO_SCENE(Structure):
    pass

_S(struct_tagNET_DVR_MATRIX_LOOP_DECINFO_SCENE, [
    ('wPoolTime', WORD),
    ('byRes1', BYTE * 2),
    ('struChanArray', NET_DVR_CYC_SUR_CHAN_ELE_SCENE * 16),
    ('byRes2', BYTE * 4),
])

NET_DVR_MATRIX_LOOP_DECINFO_SCENE = struct_tagNET_DVR_MATRIX_LOOP_DECINFO_SCENE
LPNET_DVR_MATRIX_LOOP_DECINFO_SCENE = POINTER(struct_tagNET_DVR_MATRIX_LOOP_DECINFO_SCENE)
tagNET_DVR_MATRIX_LOOP_DECINFO_SCENE = struct_tagNET_DVR_MATRIX_LOOP_DECINFO_SCENE
