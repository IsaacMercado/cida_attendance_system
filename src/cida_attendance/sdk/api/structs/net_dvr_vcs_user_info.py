from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR
from .net_dvr_associate_input_param import NET_DVR_ASSOCIATE_INPUT_PARAM
from .net_dvr_associate_output_param import NET_DVR_ASSOCIATE_OUTPUT_PARAM
from .net_dvr_rectcfg_ex import NET_DVR_RECTCFG_EX


class struct_tagNET_DVR_VCS_USER_INFO(Structure):
    pass

_S(struct_tagNET_DVR_VCS_USER_INFO, [
    ('dwSize', DWORD),
    ('sUserName', BYTE * 32),
    ('sPassWord', BYTE * 16),
    ('struUserIP', NET_DVR_IPADDR),
    ('byMacAddr', BYTE * 6),
    ('byPriority', BYTE),
    ('byRes1', BYTE),
    ('dwRight', DWORD),
    ('struInputParam', NET_DVR_ASSOCIATE_INPUT_PARAM * 1024),
    ('struOutputParam', NET_DVR_ASSOCIATE_OUTPUT_PARAM * 256),
    ('struManageRegion', NET_DVR_RECTCFG_EX),
    ('byWallNo', BYTE),
    ('byRes2', BYTE * 3),
    ('sLoginPassword', BYTE * 16),
    ('byRes', BYTE * 88),
])

NET_DVR_VCS_USER_INFO = struct_tagNET_DVR_VCS_USER_INFO
LPNET_DVR_VCS_USER_INFO = POINTER(struct_tagNET_DVR_VCS_USER_INFO)
tagNET_DVR_VCS_USER_INFO = struct_tagNET_DVR_VCS_USER_INFO
