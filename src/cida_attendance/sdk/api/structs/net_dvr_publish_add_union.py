from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_publish_ftp_cfg import NET_DVR_PUBLISH_FTP_CFG
from .net_dvr_publish_ftp_cfg_dir import NET_DVR_PUBLISH_FTP_CFG_DIR
from .net_dvr_publish_http_cfg import NET_DVR_PUBLISH_HTTP_CFG


class union_tagNET_DVR_PUBLISH_ADD_UNION(Union):
    pass

_S(union_tagNET_DVR_PUBLISH_ADD_UNION, [
    ('byLen', BYTE * 256),
    ('struHttpCfg', NET_DVR_PUBLISH_HTTP_CFG),
    ('struFtpCfg', NET_DVR_PUBLISH_FTP_CFG),
    ('struDirFtpCfg', NET_DVR_PUBLISH_FTP_CFG_DIR),
])

NET_DVR_PUBLISH_ADD_UNION = union_tagNET_DVR_PUBLISH_ADD_UNION
LPNET_DVR_PUBLISH_ADD_UNION = POINTER(union_tagNET_DVR_PUBLISH_ADD_UNION)
tagNET_DVR_PUBLISH_ADD_UNION = union_tagNET_DVR_PUBLISH_ADD_UNION
