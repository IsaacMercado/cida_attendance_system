from ctypes import Structure

from ..base_classes import _S, BYTE, DWORD, WORD
from ..ctypes_preamble import POINTER
from .anon_145 import NET_DVR_JPEGPARA
from .net_vca_single_facesnapcfg import NET_VCA_SINGLE_FACESNAPCFG


class struct_tagNET_VCA_FACESNAPCFG(Structure):
    pass

_S(struct_tagNET_VCA_FACESNAPCFG, [
    ('dwSize', DWORD),
    ('bySnapTime', BYTE),
    ('bySnapInterval', BYTE),
    ('bySnapThreshold', BYTE),
    ('byGenerateRate', BYTE),
    ('bySensitive', BYTE),
    ('byReferenceBright', BYTE),
    ('byMatchType', BYTE),
    ('byMatchThreshold', BYTE),
    ('struPictureParam', NET_DVR_JPEGPARA),
    ('struRule', NET_VCA_SINGLE_FACESNAPCFG * 8),
    ('wFaceExposureMinDuration', WORD),
    ('byFaceExposureMode', BYTE),
    ('byBackgroundPic', BYTE),
    ('dwValidFaceTime', DWORD),
    ('dwUploadInterval', DWORD),
    ('dwFaceFilteringTime', DWORD),
    ('bySceneID', BYTE),
    ('byInvalCapFilterEnable', BYTE),
    ('byInvalCapFilterThreshold', BYTE),
    ('byRes2', BYTE * 81),
])

NET_VCA_FACESNAPCFG = struct_tagNET_VCA_FACESNAPCFG
LPNET_VCA_FACESNAPCFG = POINTER(struct_tagNET_VCA_FACESNAPCFG)
tagNET_VCA_FACESNAPCFG = struct_tagNET_VCA_FACESNAPCFG
