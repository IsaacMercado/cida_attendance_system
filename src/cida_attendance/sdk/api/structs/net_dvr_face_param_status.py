from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_FACE_PARAM_STATUS(Structure):
    pass

_S(struct_tagNET_DVR_FACE_PARAM_STATUS, [
    ('dwSize', DWORD),
    ('byCardNo', BYTE * 32),
    ('byCardReaderRecvStatus', BYTE * 512),
    ('byErrorMsg', BYTE * 32),
    ('dwCardReaderNo', DWORD),
    ('byTotalStatus', BYTE),
    ('byFaceID', BYTE),
    ('byRes', BYTE * 130),
])

NET_DVR_FACE_PARAM_STATUS = struct_tagNET_DVR_FACE_PARAM_STATUS
LPNET_DVR_FACE_PARAM_STATUS = POINTER(struct_tagNET_DVR_FACE_PARAM_STATUS)
tagNET_DVR_FACE_PARAM_STATUS = struct_tagNET_DVR_FACE_PARAM_STATUS
