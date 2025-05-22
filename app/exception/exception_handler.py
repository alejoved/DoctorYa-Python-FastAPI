from fastapi import HTTPException, status

def entity_exists_exception(message: str):
    return HTTPException(
        status_code = status.HTTP_400_BAD_REQUEST,
        detail = message
    )

def entity_not_found_exception(message: str):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = message
    )

def credentials_not_valid_exception(message: str):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = message
    )