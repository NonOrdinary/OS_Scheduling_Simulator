# api/main.py

from fastapi import FastAPI
from .routes import router as api_router
from .ws import router as ws_router
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI(
    # this appears in the auto documentation page, which is very good to have
    title="OS Process Manager API with Live WS",
    version="0.1.0"
)

# Add CORS middleware
origins = [
    # list of allowed origins
    # otherwise due to policy of browser of same origin resource sharing, it won't be possible
    "http://localhost:3000", #frontend
    #"http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, OPTIONS, etc.
    allow_headers=["*"],
    # could have added authentication , but would do it in Feburary 2026
)

# HTTP routes # ac
app.include_router(api_router)

# WebSocket routes
app.include_router(ws_router)
