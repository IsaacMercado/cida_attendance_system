from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLISH_FTP_CFG(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_FTP_CFG, [
    ('byProtocolType', BYTE),
    ('byRes1', BYTE),
    ('wFTPPort', WORD),
    ('byAddress', BYTE * 64),
    ('szUserName', BYTE * 32),
    ('szPassWord', BYTE * 16),
    ('szCustomDir', BYTE * 128),
    ('byRes', BYTE * 12),
])

NET_DVR_PUBLISH_FTP_CFG = struct_tagNET_DVR_PUBLISH_FTP_CFG
LPNET_DVR_PUBLISH_FTP_CFG = POINTER(struct_tagNET_DVR_PUBLISH_FTP_CFG)
tagNET_DVR_PUBLISH_FTP_CFG = struct_tagNET_DVR_PUBLISH_FTP_CFG
