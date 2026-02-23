from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .dev_chan_info_scene import NET_DVR_DEV_CHAN_INFO_SCENE
from .stream_media_server_cfg_scene import NET_DVR_STREAM_MEDIA_SERVER_CFG_SCENE


class struct_tagPU_STREAM_CFG_SCENE(Structure):
    pass

_S(struct_tagPU_STREAM_CFG_SCENE, [
    ('streamMediaServerCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG_SCENE),
    ('struDevChanInfo', NET_DVR_DEV_CHAN_INFO_SCENE),
])

NET_DVR_PU_STREAM_CFG_SCENE = struct_tagPU_STREAM_CFG_SCENE
LPNET_DVR_PU_STREAM_CFG_SCENE = POINTER(struct_tagPU_STREAM_CFG_SCENE)
tagPU_STREAM_CFG_SCENE = struct_tagPU_STREAM_CFG_SCENE
