from src.internal.interfaces.services.auth_interface import AuthInterface
from src.constants.databases.available_databases import INITIAL_DASHBOARD


class AuthService(AuthInterface):
    def __init__(self, auth_reposiotry, database_repository):
        self.auth_reposiotry = auth_reposiotry
        self.database_repository = database_repository

    def signup(self, username: str, email: str, password: str):
        try:
            cheeck_if_user_exists = (
                self.database_repository.find_single_entity_by_field_name(
                    "users", "username", username
                )
            )
            if cheeck_if_user_exists is not None:
                return None
            save_user = self.database_repository.save_entity(
                "users", {"username": username, "email": email, "password": password}
            )
            INITIAL_DASHBOARD["username"] = username
            save_initial_dashboard = self.database_repository.save_entity(
                "configurations", INITIAL_DASHBOARD
            )

            if save_user is None or save_initial_dashboard is None:
                return None
            return save_user
        except Exception as e:
            return None

    def login(self, username: str, password: str):
        try:
            user = self.database_repository.find_single_entity_by_field_name(
                "users", "username", username
            )
            if user is None or user["password"] != password:
                return None
            access_token = self.auth_reposiotry.create_access_token({"sub": username})
            return access_token

        except Exception as e:
            return None

    def user_info(self, token: str):
        try:
            return self.auth_reposiotry.get_current_user(token)
        except Exception as e:
            return None
