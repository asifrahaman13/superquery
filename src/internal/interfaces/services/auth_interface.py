from abc import ABC, abstractmethod
from typing import Dict


class AuthInterface(ABC):

    @abstractmethod
    def create_access_token(self, data: Dict[str, str]) -> str:
        """Create an access token based on the provided data."""
        pass

    @abstractmethod
    def verify_google_access_token(self, token: str) -> Dict[str, str]:
        """Verify a Google access token and return the decoded token."""
        pass

    @abstractmethod
    def decode_access_token(self, token: str) -> Dict[str, str]:
        """Decode an access token and return the decoded token."""
        pass
