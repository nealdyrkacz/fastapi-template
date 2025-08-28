from fastapi import FastAPI
import uvicorn
import logging
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from core.config.settings import Config

from src.api.routes.server import router as server_router_v1
from src.api.routes.example import router as entity_router_v1


logging.basicConfig(
    level=Config.log_level,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)
 

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events."""
  
    # Startup
    logger.info("Starting FastApi Template App...")
    
    logger.info("Starting FastApi Template App started successfully")

    yield

    # Shutdown
    
    logger.info("Shutting down FastApi Template App...")

app = FastAPI(root_path=f"{Config.root_path}",lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Register API routes
app.include_router(server_router_v1, prefix="/v1", tags=["server"]) 
app.include_router(entity_router_v1, prefix="/v1/example", tags=["example"])