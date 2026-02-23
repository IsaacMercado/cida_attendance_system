from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_infrared_cmd_info import NET_DVR_INFRARED_CMD_INFO


class struct_tagNET_DVR_INFRARED_LEARN_CODE_CFG_(Structure):
    pass

_S(struct_tagNET_DVR_INFRARED_LEARN_CODE_CFG_, [
    ('dwSize', DWORD),
    ('sIROutName', BYTE * 32),
    ('struIRCmdInfo', NET_DVR_INFRARED_CMD_INFO * 32),
    ('byRes', BYTE * 256),
])

NET_DVR_INFRARED_CMD_NAME_CFG = struct_tagNET_DVR_INFRARED_LEARN_CODE_CFG_
LPNET_DVR_INFRARED_CMD_NAME_CFG = POINTER(struct_tagNET_DVR_INFRARED_LEARN_CODE_CFG_)
tagNET_DVR_INFRARED_LEARN_CODE_CFG_ = struct_tagNET_DVR_INFRARED_LEARN_CODE_CFG_
