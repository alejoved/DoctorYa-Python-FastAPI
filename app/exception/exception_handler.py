from fastapi import HTTPException, status


def entity_exists_exception(message: str):
    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        message = message
    )

def entity_not_exists_exception(message: str):
    return HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        message = message
    )