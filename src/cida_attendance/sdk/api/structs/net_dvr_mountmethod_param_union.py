from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_nas_mount_param import NET_DVR_NAS_MOUNT_PARAM


class union_tagNET_DVR_MOUNTMETHOD_PARAM_UNION(Union):
    pass

_S(union_tagNET_DVR_MOUNTMETHOD_PARAM_UNION, [
    ('uLen', BYTE * 56),
    ('struNasMountParam', NET_DVR_NAS_MOUNT_PARAM),
])

NET_DVR_MOUNTMETHOD_PARAM_UNION = union_tagNET_DVR_MOUNTMETHOD_PARAM_UNION
LPNET_DVR_MOUNTMETHOD_PARAM_UNION = POINTER(union_tagNET_DVR_MOUNTMETHOD_PARAM_UNION)
tagNET_DVR_MOUNTMETHOD_PARAM_UNION = union_tagNET_DVR_MOUNTMETHOD_PARAM_UNION
