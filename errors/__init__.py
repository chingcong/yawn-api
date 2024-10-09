from typing import ClassVar, AnyStr, Optional
from pydantic import BaseModel, Field

class Error(BaseModel):
    code: AnyStr = Field(..., description="Unique error code identifier")
    status: int = Field(500, description="HTTP status code")
    message: Optional[AnyStr] = Field("Please contact admin for further assistance", description="Error message")

    class Config:
        validate_assignment = True  # Ensure field validation on assignment

class Errors(BaseModel):
    InternalServerError: ClassVar[Error] = Error(
        code="INTERNAL_SERVER_ERROR",
        status=500,
        message="Internal server error"
    )
    DatabaseConnectionError: ClassVar[Error] = Error(
        code="DATABASE_CONNECTION_ERROR",
        status=500,
        message="Database connection error"
    )

errors = Errors()

