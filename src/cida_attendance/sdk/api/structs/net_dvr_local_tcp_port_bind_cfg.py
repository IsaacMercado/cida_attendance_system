from ctypes import Structure

from ..base_classes import _S, BYTE, WORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_LOCAL_TCP_PORT_BIND_CFG(Structure):
    pass

_S(struct_tagNET_DVR_LOCAL_TCP_PORT_BIND_CFG, [
    ('wLocalBindTcpMinPort', WORD),
    ('wLocalBindTcpMaxPort', WORD),
    ('byRes', BYTE * 60),
])

NET_DVR_LOCAL_TCP_PORT_BIND_CFG = struct_tagNET_DVR_LOCAL_TCP_PORT_BIND_CFG
LPNET_DVR_LOCAL_TCP_PORT_BIND_CFG = POINTER(struct_tagNET_DVR_LOCAL_TCP_PORT_BIND_CFG)
tagNET_DVR_LOCAL_TCP_PORT_BIND_CFG = struct_tagNET_DVR_LOCAL_TCP_PORT_BIND_CFG
