from ctypes import Structure, c_char

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_CMS_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_CMS_PARAM, [
    ('dwSize', DWORD),
    ('struAddr', NET_DVR_IPADDR),
    ('wServerPort', WORD),
    ('bySeverProtocolType', BYTE),
    ('byStatus', BYTE),
    ('sDeviceId', BYTE * 32),
    ('sPassWord', c_char * 16),
    ('sPlatformEhomeVersion', BYTE * 32),
    ('byNetWork', BYTE),
    ('byAddressType', BYTE),
    ('byProtocolVersion', BYTE),
    ('byRes1', BYTE),
    ('sDomainName', BYTE * 64),
    ('byEnable', BYTE),
    ('byRes', BYTE * 139),
])

NET_DVR_CMS_PARAM = struct_tagNET_DVR_CMS_PARAM
LPNET_DVR_CMS_PARAM = POINTER(struct_tagNET_DVR_CMS_PARAM)
tagNET_DVR_CMS_PARAM = struct_tagNET_DVR_CMS_PARAM
