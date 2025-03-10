from fastapi import APIRouter, HTTPException
from fastapi import File, UploadFile
from botocore.exceptions import NoCredentialsError
from fastapi import Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.exports import get_auth_service, get_aws_service
from src.use_cases import FileService, AuthService
from fastapi.responses import JSONResponse

security = HTTPBearer()

upload_controller = APIRouter()


@upload_controller.post("/aws-file-upload", response_model=dict)
async def upload_file(
    file: UploadFile = File(...),
    credentials: HTTPAuthorizationCredentials = Security(security),
    auth_service: AuthService = Depends(get_auth_service),
    file_service: FileService = Depends(get_aws_service),
):
    token = credentials.credentials
    user = auth_service.user_info(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    try:
        response = await file_service.upload_file(
            user["sub"], f"{user['sub']}_{file.filename}", file.file
        )
        return JSONResponse(content={"message": response})
    except NoCredentialsError:
        raise HTTPException(status_code=400, detail="Credentials not available")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")


@upload_controller.get("/aws-file-url", response_model=dict)
async def get_presigned_url(
    credentials: HTTPAuthorizationCredentials = Security(security),
    auth_service: AuthService = Depends(get_auth_service),
    file_service: FileService = Depends(get_aws_service),
):
    token = credentials.credentials
    user = auth_service.user_info(token)
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    try:
        url = await file_service.get_presigned_urls(user["sub"])
        return JSONResponse(content={"url": url})
    except NoCredentialsError:
        raise HTTPException(status_code=400, detail="Credentials not available")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred: {str(e)}")
