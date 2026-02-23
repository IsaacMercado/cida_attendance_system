from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD
from ..ctypes_preamble import POINTER
from .net_dvr_cert_name import NET_DVR_CERT_NAME
from .net_dvr_cert_param import NET_DVR_CERT_PARAM
from .net_dvr_time_ex import NET_DVR_TIME_EX


class struct_tagNET_DVR_CERT_INFO(Structure):
    pass

_S(struct_tagNET_DVR_CERT_INFO, [
    ('dwSize', DWORD),
    ('struCertParam', NET_DVR_CERT_PARAM),
    ('dwValidDays', DWORD),
    ('byPasswd', BYTE * 32),
    ('struCertName', NET_DVR_CERT_NAME),
    ('struIssuerName', NET_DVR_CERT_NAME),
    ('struBeginTime', NET_DVR_TIME_EX),
    ('struEndTime', NET_DVR_TIME_EX),
    ('serialNumber', BYTE * 32),
    ('byVersion', BYTE),
    ('byKeyAlgorithm', BYTE),
    ('byKeyLen', BYTE),
    ('bySignatureAlgorithm', BYTE),
    ('byRes', BYTE * 128),
])

NET_DVR_CERT_INFO = struct_tagNET_DVR_CERT_INFO
LPNET_DVR_CERT_INFO = POINTER(struct_tagNET_DVR_CERT_INFO)
tagNET_DVR_CERT_INFO = struct_tagNET_DVR_CERT_INFO
