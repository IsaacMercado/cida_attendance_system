from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_SMSCONTENT(Structure):
    pass

_S(struct_tagNET_DVR_SMSCONTENT, [
    ('byPhoneNum', BYTE * 32),
    ('byMsg', BYTE * 140),
])

NET_DVR_SMSCONTENT = struct_tagNET_DVR_SMSCONTENT
LPNET_DVR_SMSCONTENT = POINTER(struct_tagNET_DVR_SMSCONTENT)
tagNET_DVR_SMSCONTENT = struct_tagNET_DVR_SMSCONTENT
