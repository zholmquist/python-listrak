from listrak.api_operations.all import All
from listrak.api_operations.find import Find
from listrak.api_operations.find_all import FindAll

from listrak.service.base_service import BaseService

from listrak.schemas import contact


class Contacts(BaseService, All, Find, FindAll):
    schema = contact.Contact
