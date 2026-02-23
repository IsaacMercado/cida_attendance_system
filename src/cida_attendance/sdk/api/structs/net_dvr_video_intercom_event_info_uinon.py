from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_auth_info import NET_DVR_AUTH_INFO
from .net_dvr_magnetic_door_status import NET_DVR_MAGNETIC_DOOR_STATUS
from .net_dvr_noticedata_receipt_info import NET_DVR_NOTICEDATA_RECEIPT_INFO
from .net_dvr_send_card_info import NET_DVR_SEND_CARD_INFO
from .net_dvr_unlock_record_info import NET_DVR_UNLOCK_RECORD_INFO
from .net_dvr_upload_plate_info import NET_DVR_UPLOAD_PLATE_INFO


class union_tagNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON(Union):
    pass

_S(union_tagNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON, [
    ('byLen', BYTE * 256),
    ('struUnlockRecord', NET_DVR_UNLOCK_RECORD_INFO),
    ('struNoticedataReceipt', NET_DVR_NOTICEDATA_RECEIPT_INFO),
    ('struAuthInfo', NET_DVR_AUTH_INFO),
    ('struUploadPlateInfo', NET_DVR_UPLOAD_PLATE_INFO),
    ('struSendCardInfo', NET_DVR_SEND_CARD_INFO),
    ('struMagneticDoorStatus', NET_DVR_MAGNETIC_DOOR_STATUS),
])

NET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON = union_tagNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON
LPNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON = POINTER(union_tagNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON)
tagNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON = union_tagNET_DVR_VIDEO_INTERCOM_EVENT_INFO_UINON
