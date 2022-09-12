from datetime import datetime
from enum import Enum
from typing import Optional

from listrak.schemas.api_resource import Resource


class BoundHandler(str, Enum):
    none = "None"  # "Do Not Handle"
    standard = "Standard"
    aggressive = "Aggressive"


class List(Resource):
    listId: Optional[int]
    createDate: Optional[datetime]
    folderId: Optional[int]
    ipPoolId: Optional[int]

    bounceUnsubscribeCount: Optional[int]  # Unsubscribe all users after X consectuive
    bounceHandling: BoundHandler
    bounceDomainAlias: Optional[str]

    listName: Optional[str]
    fromEmail: Optional[str]
    fromName: Optional[str]

    linkDomainAlias: Optional[str]
    mediaDomainAlias: Optional[str]  # should be URL, but no scheme

    googleTrackingDomains: Optional[list]

    enableBrowserLink: Optional[bool]
    enableDoubleOptIn: Optional[bool]
    enableGoogleAnalytics: Optional[bool]
    enableInternationalization: Optional[bool]
    enableListHygiene: Optional[bool]
    enableListRemovalHeader: Optional[bool]
    enableListRemovalLink: Optional[bool]
    enableListrakAnalytics: Optional[bool]
    enableSpamScorePersonalization: Optional[bool]
    enableToNamePersonalization: Optional[bool]
    enableUniversalEmailKeySetting: Optional[bool]

    class Config:
        use_enum_values = True
