from src.constants.databases.available_databases import INITIAL_DASHBOARD


class AuthService:
    def __init__(self, auth_repo, database_repo):
        self.auth_repo = auth_repo
        self.database_repo = database_repo

    async def signup(self, username: str, email: str, password: str):
        try:
            cheeck_if_user_exists = (
                await self.database_repo.find_single_entity_by_field_name(
                    "users", "username", username
                )
            )

            if cheeck_if_user_exists is not None:
                return None
            save_user = await self.database_repo.save_entity(
                "users", {"username": username, "email": email, "password": password}
            )
            INITIAL_DASHBOARD["username"] = username
            save_initial_dashboard = await self.database_repo.save_entity(
                "configurations", INITIAL_DASHBOARD
            )

            if save_user is None or save_initial_dashboard is None:
                return None
            return save_user
        except Exception:
            return None

    async def login(self, username: str, password: str):
        try:
            user = await self.database_repo.find_single_entity_by_field_name(
                "users", "username", username
            )
            if user is None or user["password"] != password:
                return None
            access_token = self.auth_repo.create_access_token({"sub": username})
            return access_token

        except Exception:
            raise

    def user_info(self, token: str):
        return self.auth_repo.get_current_user(token)
