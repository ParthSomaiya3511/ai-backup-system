from fastapi import FastAPI

from app.api.routes.backup import router as backup_router
from app.api.routes.recovery import router as recovery_router
from app.api.routes.ai import router as ai_router
from app.api.routes.security import router as security_router
from app.auth.routes import router as auth_router

app = FastAPI(
    title="AI Backup System",
    version="1.0.0"
)

app.include_router(backup_router, prefix="/api", tags=["Backup"])
app.include_router(recovery_router, prefix="/api", tags=["Recovery"])
app.include_router(ai_router, prefix="/api", tags=["AI"])
app.include_router(security_router, prefix="/api", tags=["Security"])
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])


@app.get("/")
def root():

    return {
        "status": "running",
        "application": "AI Backup System",
        "version": "1.0.0"
    }