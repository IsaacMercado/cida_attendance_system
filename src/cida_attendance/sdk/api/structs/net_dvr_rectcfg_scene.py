from ctypes import Structure

from ..base_classes import _S, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_RECTCFG_SCENE(Structure):
    pass

_S(struct_tagNET_DVR_RECTCFG_SCENE, [
    ('wXCoordinate', WORD),
    ('wYCoordinate', WORD),
    ('wWidth', WORD),
    ('wHeight', WORD),
])

NET_DVR_RECTCFG_SCENE = struct_tagNET_DVR_RECTCFG_SCENE
LPNET_DVR_RECTCFGSCENE = POINTER(struct_tagNET_DVR_RECTCFG_SCENE)
tagNET_DVR_RECTCFG_SCENE = struct_tagNET_DVR_RECTCFG_SCENE
