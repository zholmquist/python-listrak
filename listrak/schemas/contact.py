from datetime import datetime
from enum import Enum
from typing import Optional

from listrak.schemas.api_resource import Resource


class Contact(Resource):
    emailAddress: Optional[str]
