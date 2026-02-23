from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_ILLEGALCARDFILTERING_CFG(Structure):
    pass

_S(struct_tagNET_DVR_ILLEGALCARDFILTERING_CFG, [
    ('dwSize', DWORD),
    ('sLEDDefaultInfo', c_char * 512),
    ('byillegalCardFilteringEnabled', BYTE),
    ('bySendCardSensingCoilEnabled', BYTE),
    ('byWiegendSensingCoilEnabled', BYTE),
    ('byGateSwitchEnabled', BYTE),
    ('byVerifyKeyWriteCardEnabled', BYTE),
    ('byNoplateTakeCardEnabled', BYTE),
    ('byRes', BYTE * 126),
])

NET_DVR_ILLEGALCARDFILTERING_CFG = struct_tagNET_DVR_ILLEGALCARDFILTERING_CFG
LPNET_DVR_ILLEGALCARDFILTERING_CFG = POINTER(struct_tagNET_DVR_ILLEGALCARDFILTERING_CFG)
tagNET_DVR_ILLEGALCARDFILTERING_CFG = struct_tagNET_DVR_ILLEGALCARDFILTERING_CFG
