from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_2 import NET_DVR_IPADDR


class struct_tagNET_DVR_ENCODE_JOINT_PARAM(Structure):
    pass

_S(struct_tagNET_DVR_ENCODE_JOINT_PARAM, [
    ('dwSize', DWORD),
    ('byJointed', BYTE),
    ('byDevType', BYTE),
    ('byRes1', BYTE * 2),
    ('struIP', NET_DVR_IPADDR),
    ('wPort', WORD),
    ('wChannel', WORD),
    ('byRes2', BYTE * 20),
])

NET_DVR_ENCODE_JOINT_PARAM = struct_tagNET_DVR_ENCODE_JOINT_PARAM
LPNET_DVR_ENCODE_JOINT_PARAM = POINTER(struct_tagNET_DVR_ENCODE_JOINT_PARAM)
tagNET_DVR_ENCODE_JOINT_PARAM = struct_tagNET_DVR_ENCODE_JOINT_PARAM
