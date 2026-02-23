from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_inquest_pip_param_v40 import NET_DVR_INQUEST_PIP_PARAM_V40
from .net_dvr_structhead import NET_DVR_STRUCTHEAD


class struct_tagNET_DVR_INQUEST_PIP_STATUS_V40(Structure):
    pass

_S(struct_tagNET_DVR_INQUEST_PIP_STATUS_V40, [
    ('struStructHead', NET_DVR_STRUCTHEAD),
    ('byBaseChan', BYTE),
    ('byBackChan', BYTE),
    ('byPIPMode', BYTE),
    ('byPipCount', BYTE),
    ('byPicShowMode', BYTE),
    ('byRes', BYTE * 31),
    ('strPipPara', NET_DVR_INQUEST_PIP_PARAM_V40 * 16),
])

NET_DVR_INQUEST_PIP_STATUS_V40 = struct_tagNET_DVR_INQUEST_PIP_STATUS_V40
LPNET_DVR_INQUEST_PIP_STATUS_V40 = POINTER(struct_tagNET_DVR_INQUEST_PIP_STATUS_V40)
tagNET_DVR_INQUEST_PIP_STATUS_V40 = struct_tagNET_DVR_INQUEST_PIP_STATUS_V40
