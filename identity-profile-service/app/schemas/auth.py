from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "member"


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class CurrentUserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool
    totp_enabled: bool


class MfaSetupResponse(BaseModel):
    totp_secret: str
    provisioning_uri: str


class MfaVerifyRequest(BaseModel):
    code: str


class MfaStatusResponse(BaseModel):
    totp_enabled: bool
