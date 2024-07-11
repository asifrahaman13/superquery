from abc import ABC, abstractmethod


class AuthInterface(ABC):
    @abstractmethod
    def signup(self, username: str, email: str, password: str):
        pass

    @abstractmethod
    def login(self, username: str, password: str):
        pass

    @abstractmethod
    def user_info(self, token: str):
        pass
