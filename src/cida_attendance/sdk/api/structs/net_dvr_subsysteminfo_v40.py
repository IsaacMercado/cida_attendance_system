from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_SUBSYSTEMINFO_V40(Structure):
    pass

_S(struct_tagNET_DVR_SUBSYSTEMINFO_V40, [
    ('bySubSystemType', BYTE),
    ('byChan', BYTE),
    ('byLoginType', BYTE),
    ('bySlotNum', BYTE),
    ('byRes1', BYTE * 4),
    ('struSubSystemIP', NET_DVR_IPADDR),
    ('struSubSystemIPMask', NET_DVR_IPADDR),
    ('struGatewayIpAddr', NET_DVR_IPADDR),
    ('wSubSystemPort', WORD),
    ('byRes2', BYTE * 6),
    ('sUserName', BYTE * 32),
    ('sPassword', BYTE * 16),
    ('sDomainName', c_char * 64),
    ('sDnsAddress', c_char * 64),
    ('sSerialNumber', BYTE * 48),
    ('byBelongBoard', BYTE),
    ('byInterfaceType', BYTE),
    ('byInterfaceNums', BYTE),
    ('byInterfaceStartNum', BYTE),
    ('byDeviceName', BYTE * 20),
    ('byAudioChanNums', BYTE),
    ('byAudioChanStartNum', BYTE),
    ('byAudioChanType', BYTE),
    ('byRes3', BYTE * 33),
])

NET_DVR_SUBSYSTEMINFO_V40 = struct_tagNET_DVR_SUBSYSTEMINFO_V40
LPNET_DVR_SUBSYSTEMINFO_V40 = POINTER(struct_tagNET_DVR_SUBSYSTEMINFO_V40)
tagNET_DVR_SUBSYSTEMINFO_V40 = struct_tagNET_DVR_SUBSYSTEMINFO_V40
