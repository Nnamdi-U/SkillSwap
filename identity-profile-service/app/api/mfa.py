import pyotp
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.auth import get_current_user
from app.core.config import settings
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import MfaSetupResponse, MfaStatusResponse, MfaVerifyRequest

router = APIRouter(prefix="/api/v1/mfa", tags=["mfa"])


@router.post("/setup", response_model=MfaSetupResponse)
def setup_mfa(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current_user.totp_enabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MFA is already enabled")

    secret = pyotp.random_base32()
    current_user.totp_secret = secret
    db.commit()
    db.refresh(current_user)

    provisioning_uri = pyotp.TOTP(secret).provisioning_uri(
        name=current_user.email,
        issuer_name=settings.mfa_issuer_name,
    )
    return MfaSetupResponse(totp_secret=secret, provisioning_uri=provisioning_uri)


@router.post("/verify", response_model=MfaStatusResponse)
def verify_mfa(
    verify_data: MfaVerifyRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not current_user.totp_secret:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="MFA setup has not been started")

    is_valid_code = pyotp.TOTP(current_user.totp_secret).verify(verify_data.code)
    if not is_valid_code:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid MFA code")

    current_user.totp_enabled = True
    db.commit()
    db.refresh(current_user)
    return MfaStatusResponse(totp_enabled=current_user.totp_enabled)
