from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_mount_param_union import NET_DVR_MOUNT_PARAM_UNION


class struct_tagNET_DVR_NAS_MOUNT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_NAS_MOUNT_PARAM, [
    ('byMountType', BYTE),
    ('byRes', BYTE * 3),
    ('uMountParam', NET_DVR_MOUNT_PARAM_UNION),
])

NET_DVR_NAS_MOUNT_PARAM = struct_tagNET_DVR_NAS_MOUNT_PARAM
LPNET_DVR_NAS_MOUNT_PARAM = POINTER(struct_tagNET_DVR_NAS_MOUNT_PARAM)
tagNET_DVR_NAS_MOUNT_PARAM = struct_tagNET_DVR_NAS_MOUNT_PARAM
