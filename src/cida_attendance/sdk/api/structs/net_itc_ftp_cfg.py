from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_297 import NET_DVR_PICTURE_NAME
from .anon_345 import union_anon_345


class struct_tagNET_ITC_FTP_CFG(Structure):
    pass

_S(struct_tagNET_ITC_FTP_CFG, [
    ('dwSize', DWORD),
    ('byEnable', BYTE),
    ('byAddressType', BYTE),
    ('wFTPPort', WORD),
    ('unionServer', union_anon_345),
    ('szUserName', BYTE * 32),
    ('szPassWORD', BYTE * 16),
    ('byRes4', BYTE),
    ('byDirLevel', BYTE),
    ('byIsFilterCarPic', BYTE),
    ('byUploadDataType', BYTE),
    ('struPicNameRule', NET_DVR_PICTURE_NAME),
    ('byTopDirMode', BYTE),
    ('bySubDirMode', BYTE),
    ('byThreeDirMode', BYTE),
    ('byFourDirMode', BYTE),
    ('szPicNameCustom', BYTE * 32),
    ('szTopCustomDir', BYTE * 32),
    ('szSubCustomDir', BYTE * 32),
    ('szThreeCustomDir', BYTE * 32),
    ('szFourCustomDir', BYTE * 32),
    ('byRes3', BYTE * 900),
])

NET_ITC_FTP_CFG = struct_tagNET_ITC_FTP_CFG
LPNET_ITC_FTP_CFG = POINTER(struct_tagNET_ITC_FTP_CFG)
tagNET_ITC_FTP_CFG = struct_tagNET_ITC_FTP_CFG
