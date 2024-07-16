from typing import Any
from src.internal.interfaces.services.file_interface import FileInterface


class FileService(FileInterface):

    def __init__(self, database_repository, aws_repository) -> None:
        self.database_repository = database_repository
        self.aws_repository = aws_repository

    def upload_file(self, username: str, file_name: str, file_content: Any) -> None:
        mongodb_upload = self.database_repository.save_entity(
            "aws", {"username": username, "file_name": file_name}
        )
        aws_upload = self.aws_repository.upload_file(file_name, file_content)
        if mongodb_upload and aws_upload:
            return True
        return False

    def all_aws_files(self, username: str):
        all_aws_file_names = self.database_repository.find_all_entities_by_field_name(
            "aws", "username", username
        )
        return all_aws_file_names

    def get_presigned_urls(self, username: str) -> str:
        all_aws_file_names = self.database_repository.find_all_entities_by_field_name(
            "aws", "username", username
        )
        all_presigned_urls = []
        for index, item in enumerate(all_aws_file_names):
            file_name = item["file_name"]
            print(index, file_name)
            all_presigned_urls.append(self.aws_repository.get_presigned_urls(file_name))

        return all_presigned_urls
