from fastapi import HTTPException, status


class HttePrequestErrors:

    def bad_request():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid input"
        )

    def unauthorized():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
        )

    def forbidden():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access forbidden"
        )

    def detail_not_found():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, details="Details not found"
        )

    def internal_server_error():
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server error",
        )
