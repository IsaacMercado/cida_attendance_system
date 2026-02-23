from ctypes import Union

from ..base_classes import _S, BYTE
from ..ctypes_preamble import POINTER
from .net_dvr_behaviour_cond import NET_DVR_BEHAVIOUR_COND
from .net_dvr_face_pic_data_info import NET_DVR_FACE_PIC_DATA_INFO
from .net_dvr_vehicle_para import NET_DVR_VEHICLE_PARA
from .net_vca_human_feature import NET_VCA_HUMAN_FEATURE


class union_tagNET_DVR_SMARTSEARCH_PIC_UNION(Union):
    pass

_S(union_tagNET_DVR_SMARTSEARCH_PIC_UNION, [
    ('byLen', BYTE * 256),
    ('struVehiclePara', NET_DVR_VEHICLE_PARA),
    ('struHumaFeature', NET_VCA_HUMAN_FEATURE),
    ('struHumaPic', NET_DVR_FACE_PIC_DATA_INFO),
    ('struBehaviourCond', NET_DVR_BEHAVIOUR_COND),
])

NET_DVR_SMARTSEARCH_PIC_UNION = union_tagNET_DVR_SMARTSEARCH_PIC_UNION
LPNET_DVR_SMARTSEARCH_PIC_UNION = POINTER(union_tagNET_DVR_SMARTSEARCH_PIC_UNION)
tagNET_DVR_SMARTSEARCH_PIC_UNION = union_tagNET_DVR_SMARTSEARCH_PIC_UNION
