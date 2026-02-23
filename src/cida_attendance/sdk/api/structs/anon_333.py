from ctypes import Union

from ..base_classes import _S
from .net_dvr_matrix_loop_decinfo_scene import NET_DVR_MATRIX_LOOP_DECINFO_SCENE
from .pu_stream_cfg_scene import NET_DVR_PU_STREAM_CFG_SCENE


class union_anon_333(Union):
    pass

_S(union_anon_333, [
    ('struSceneDynamicDecCfg', NET_DVR_PU_STREAM_CFG_SCENE),
    ('struSceneCycDecCfg', NET_DVR_MATRIX_LOOP_DECINFO_SCENE),
])

