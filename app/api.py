import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.config import get_settings
from logging_config import setup_logging

settings = get_settings()
setup_logging(getattr(settings, "LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        logger.info("Initializing database...")
        logger.info("Application startup completed successfully")
    except Exception as e:
        logger.error(f"Startup failed: {str(e)}")
        raise
    yield
    # Shutdown
    logger.info("Application shutting down...")


def create_application() -> FastAPI:
    """
    Create and configure FastAPI application.
    
    Returns:
        FastAPI: Configured application instance
    """
    
    app = FastAPI(
        title=settings.APP_NAME or "Prism API",
        description=settings.APP_DESCRIPTION or "Prism API",
        version=settings.API_VERSION or "v1",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        lifespan=lifespan,
    )

    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routes
    app.include_router(home_router.home_route, tags=["home"])

    return app

app = create_application()

if __name__ == '__main__':
    setup_logging("DEBUG")
    uvicorn.run(
        'api:app',
        host='0.0.0.0',
        port=8081,
        reload=True,
        log_level="info"
    )