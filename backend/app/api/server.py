from fastapi import FastAPI

from api.routes.backup import router as backup_router
from api.routes.recovery import router as recovery_router
from auth.routes import router as auth_router
from api.routes.ai import router as ai_router
from api.routes.security import (
    router as security_router
)


app = FastAPI()

app.include_router(
    backup_router,
    prefix="/api"
)

app.include_router(
    recovery_router,
    prefix="/api"
)

app.include_router(
    ai_router,
    prefix="/api"
)


app.include_router(
    auth_router,
    prefix="/api/auth"
)

app.include_router(

    security_router,
    prefix="/api"
)