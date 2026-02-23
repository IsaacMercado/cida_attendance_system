from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_PUBLISH_FTP_CFG_DIR(Structure):
    pass

_S(struct_tagNET_DVR_PUBLISH_FTP_CFG_DIR, [
    ('byProtocolType', BYTE),
    ('byRes1', BYTE),
    ('wFTPPort', WORD),
    ('byAddress', BYTE * 64),
    ('szUserName', BYTE * 32),
    ('szPassWord', BYTE * 16),
    ('byDirLevel', BYTE),
    ('byTopDirMode', BYTE),
    ('bySubDirMode', BYTE),
    ('byRes2', BYTE),
    ('byTopCustomDir', BYTE * 32),
    ('bySubCustomDir', BYTE * 32),
    ('byRes', BYTE * 72),
])

NET_DVR_PUBLISH_FTP_CFG_DIR = struct_tagNET_DVR_PUBLISH_FTP_CFG_DIR
LPNET_DVR_PUBLISH_FTP_CFG_DIR = POINTER(struct_tagNET_DVR_PUBLISH_FTP_CFG_DIR)
tagNET_DVR_PUBLISH_FTP_CFG_DIR = struct_tagNET_DVR_PUBLISH_FTP_CFG_DIR
