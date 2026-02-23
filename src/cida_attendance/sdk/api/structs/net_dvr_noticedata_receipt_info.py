from ctypes import Structure

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER


class struct_tagNET_DVR_NOTICEDATA_RECEIPT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_NOTICEDATA_RECEIPT_INFO, [
    ('byNoticeNumber', BYTE * 32),
    ('byRes', BYTE * 224),
])

NET_DVR_NOTICEDATA_RECEIPT_INFO = struct_tagNET_DVR_NOTICEDATA_RECEIPT_INFO
LPNET_DVR_NOTICEDATA_RECEIPT_INFO = POINTER(struct_tagNET_DVR_NOTICEDATA_RECEIPT_INFO)
tagNET_DVR_NOTICEDATA_RECEIPT_INFO = struct_tagNET_DVR_NOTICEDATA_RECEIPT_INFO
