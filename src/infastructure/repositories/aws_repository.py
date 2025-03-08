import logging
import boto3


class AWSRepo:
    def __init__(
        self, aws_bucket_name: str, aws_access_key_id: str, aws_secret_access_key: str
    ):
        self.__aws_bucket_name = aws_bucket_name
        self.__s3_client = boto3.client(
            "s3",
            region_name="us-east-1",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
        )
        self.expiration_time = 60

    def upload_file(self, file_name: str, file_content: str):
        try:
            self.__s3_client.upload_fileobj(
                file_content, self.__aws_bucket_name, file_name
            )
            return True
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return False

    def get_presigned_urls(self, file_name: str):
        try:
            url = self.__s3_client.generate_presigned_url(
                ClientMethod="get_object",
                Params={
                    "Bucket": self.__aws_bucket_name,
                    "Key": file_name,
                    "ResponseContentDisposition": "inline",
                    "ResponseContentType": "image/png",
                },
                ExpiresIn=self.expiration_time,
            )
            logging.info(url)
            return url
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return None
