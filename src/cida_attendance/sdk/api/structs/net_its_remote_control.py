from ctypes import Structure

from ..base_classes import _S, DWORD
from ..ctypes_preamble import POINTER
from .net_its_remote_command import NET_ITS_REMOTE_COMMAND


class struct_tagNET_ITS_REMOTE_CONTROL_(Structure):
    pass

_S(struct_tagNET_ITS_REMOTE_CONTROL_, [
    ('dwSize', DWORD),
    ('struRemoteCommand', NET_ITS_REMOTE_COMMAND),
])

NET_ITS_REMOTE_CONTROL = struct_tagNET_ITS_REMOTE_CONTROL_
LPNET_ITS_REMOTE_CONTROL = POINTER(struct_tagNET_ITS_REMOTE_CONTROL_)
tagNET_ITS_REMOTE_CONTROL_ = struct_tagNET_ITS_REMOTE_CONTROL_
