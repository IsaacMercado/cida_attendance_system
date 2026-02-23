from ctypes import Structure

from ..base_classes import _S
from ..ctypes_preamble import POINTER
from .anon_6 import NET_DVR_SCHEDTIME
from .net_dvr_pu_stream_cfg import NET_DVR_PU_STREAM_CFG


class struct_tagNET_IVMS_DEVSCHED(Structure):
    pass

_S(struct_tagNET_IVMS_DEVSCHED, [
    ('struTime', NET_DVR_SCHEDTIME),
    ('struPUStream', NET_DVR_PU_STREAM_CFG),
])

NET_IVMS_DEVSCHED = struct_tagNET_IVMS_DEVSCHED
LPNET_IVMS_DEVSCHED = POINTER(struct_tagNET_IVMS_DEVSCHED)
tagNET_IVMS_DEVSCHED = struct_tagNET_IVMS_DEVSCHED
