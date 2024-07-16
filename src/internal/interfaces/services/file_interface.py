from abc import ABC, abstractmethod
from typing import Any


class FileInterface(ABC):
    @abstractmethod
    def upload_file(self, username: str, file_name: str, file_content: Any) -> None:
        pass

    @abstractmethod
    def get_presigned_urls(self, username: str) -> str:
        pass
