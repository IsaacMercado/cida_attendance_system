from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_298 import NET_DVR_PICTURE_NAME_EX
from .anon_369 import union_anon_369
from .net_dvr_structhead import NET_DVR_STRUCTHEAD


class struct_tagNET_DVR_FTPCFG_V40(Structure):
    pass

_S(struct_tagNET_DVR_FTPCFG_V40, [
    ('struStruceHead', NET_DVR_STRUCTHEAD),
    ('byEnableFTP', BYTE),
    ('byProtocolType', BYTE),
    ('wFTPPort', WORD),
    ('unionServer', union_anon_369),
    ('szUserName', BYTE * 32),
    ('szPassWORD', BYTE * 16),
    ('szTopCustomDir', BYTE * 64),
    ('szSubCustomDir', BYTE * 64),
    ('byDirLevel', BYTE),
    ('byTopDirMode', BYTE),
    ('bySubDirMode', BYTE),
    ('byType', BYTE),
    ('byEnableAnony', BYTE),
    ('byAddresType', BYTE),
    ('byFTPPicType', BYTE),
    ('byPicArchivingInterval', BYTE),
    ('struPicNameRule', NET_DVR_PICTURE_NAME_EX),
    ('byPicNameRuleType', BYTE),
    ('byRes', BYTE * 203),
])

NET_DVR_FTPCFG_V40 = struct_tagNET_DVR_FTPCFG_V40
LPNET_DVR_FTPCFG_V40 = POINTER(struct_tagNET_DVR_FTPCFG_V40)
tagNET_DVR_FTPCFG_V40 = struct_tagNET_DVR_FTPCFG_V40
