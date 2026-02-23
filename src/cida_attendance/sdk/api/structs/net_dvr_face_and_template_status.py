from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACE_AND_TEMPLATE_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_FACE_AND_TEMPLATE_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byRecvStatus', BYTE),
    ('byRes', BYTE * 131),
])

NET_DVR_FACE_AND_TEMPLATE_STATUS = struct_tagNET_DVR_FACE_AND_TEMPLATE_STATUS
LPNET_DVR_FACE_AND_TEMPLATE_STATUS = POINTER(struct_tagNET_DVR_FACE_AND_TEMPLATE_STATUS)
tagNET_DVR_FACE_AND_TEMPLATE_STATUS = struct_tagNET_DVR_FACE_AND_TEMPLATE_STATUS
