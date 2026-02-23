from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_noamal_sub_system import NET_DVR_NOAMAL_SUB_SYSTEM
from .net_dvr_public_sub_system import NET_DVR_PUBLIC_SUB_SYSTEM


class union_tagNET_DVR_JOINT_SUB_SYSTEM(Union):
    pass

_S(union_tagNET_DVR_JOINT_SUB_SYSTEM, [
    ('struNormalSubSystem', NET_DVR_NOAMAL_SUB_SYSTEM),
    ('struPublicSubSystem', NET_DVR_PUBLIC_SUB_SYSTEM),
    ('byRes', BYTE * 20),
])

NET_DVR_JOINT_SUB_SYSTEM = union_tagNET_DVR_JOINT_SUB_SYSTEM
LPNET_DVR_JOINT_SUB_SYSTEM = POINTER(union_tagNET_DVR_JOINT_SUB_SYSTEM)
tagNET_DVR_JOINT_SUB_SYSTEM = union_tagNET_DVR_JOINT_SUB_SYSTEM
