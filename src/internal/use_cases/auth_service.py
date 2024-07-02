from src.internal.interfaces.services.auth_interface import AuthInterface


class AuthService(AuthInterface):
    def __init__(self, auth_reposiotry, database_repository):
        self.auth_reposiotry = auth_reposiotry
        self.database_repository = database_repository

    def singup(self, username: str, email: str, password: str):
        try:
            save_user = self.database_repository.save_entity(
                "users", {"username": username, "email": email, "password": password}
            )
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
            print("###################", token)
            return self.auth_reposiotry.get_current_user(token)
        except Exception as e:
            return None
