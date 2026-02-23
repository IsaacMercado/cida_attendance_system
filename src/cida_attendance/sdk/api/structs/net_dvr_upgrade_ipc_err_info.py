from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .net_dvr_upgrade_ipc_err_info_single import NET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE


class struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO(Structure):
    pass

_S(struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO, [
    ('struErrInfoSingle', NET_DVR_UPGRADE_IPC_ERR_INFO_SINGLE * int((32 + 32))),
])

NET_DVR_UPGRADE_IPC_ERR_INFO = struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO
LPNET_DVR_UPGRADE_IPC_ERR_INFO = POINTER(struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO)
tagNET_DVR_UPGRADE_IPC_ERR_INFO = struct_tagNET_DVR_UPGRADE_IPC_ERR_INFO
