from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .dev_chan_info_scene import NET_DVR_DEV_CHAN_INFO_SCENE
from .stream_media_server_cfg_scene import NET_DVR_STREAM_MEDIA_SERVER_CFG_SCENE


class struct_tagNET_DVR_CYC_SUR_CHAN_ELE_SCENE(Structure):
    pass

_S(struct_tagNET_DVR_CYC_SUR_CHAN_ELE_SCENE, [
    ('byEnable', BYTE),
    ('byRes', BYTE * 3),
    ('struStreamMediaSvrCfg', NET_DVR_STREAM_MEDIA_SERVER_CFG_SCENE),
    ('struDecChanInfo', NET_DVR_DEV_CHAN_INFO_SCENE),
])

NET_DVR_CYC_SUR_CHAN_ELE_SCENE = struct_tagNET_DVR_CYC_SUR_CHAN_ELE_SCENE
LPNET_DVR_CYC_SUR_CHAN_ELE_SCENE = POINTER(struct_tagNET_DVR_CYC_SUR_CHAN_ELE_SCENE)
tagNET_DVR_CYC_SUR_CHAN_ELE_SCENE = struct_tagNET_DVR_CYC_SUR_CHAN_ELE_SCENE
