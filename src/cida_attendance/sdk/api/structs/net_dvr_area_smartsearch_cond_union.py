from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_facedetection_searchcond import NET_DVR_FACEDETECTION_SEARCHCOND
from .net_dvr_intrusion_searchcond import NET_DVR_INTRUSION_SEARCHCOND
from .net_dvr_traverse_plane_searchcond import NET_DVR_TRAVERSE_PLANE_SEARCHCOND


class union_tagNET_DVR_AREA_SMARTSEARCH_COND_UNION(Union):
    pass

_S(union_tagNET_DVR_AREA_SMARTSEARCH_COND_UNION, [
    ('byLen', BYTE * 6144),
    ('byMotionScope', (BYTE * 96) * 64),
    ('struTraversPlaneCond', NET_DVR_TRAVERSE_PLANE_SEARCHCOND),
    ('struIntrusionCond', NET_DVR_INTRUSION_SEARCHCOND),
    ('struFaceSnapCond', NET_DVR_FACEDETECTION_SEARCHCOND),
])

NET_DVR_AREA_SMARTSEARCH_COND_UNION = union_tagNET_DVR_AREA_SMARTSEARCH_COND_UNION
LPNET_DVR_AREA_SMARTSEARCH_COND_UNION = POINTER(union_tagNET_DVR_AREA_SMARTSEARCH_COND_UNION)
tagNET_DVR_AREA_SMARTSEARCH_COND_UNION = union_tagNET_DVR_AREA_SMARTSEARCH_COND_UNION
