from listrak.api_operations.all import All
from listrak.api_operations.find import Find
from listrak.api_operations.find_all import FindAll

from listrak.service.base_service import BaseService

from listrak.schemas import list


class Lists(BaseService, All, Find, FindAll):
    schema = list.List
