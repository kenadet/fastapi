from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.item.routes import router as item_router


app = FastAPI(title="Item api", version="1.0.1")

# app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all domains. You can specify specific domains like ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(item_router)

if __name__ == "__main__":
    uvicorn.run("app:main", host="0.0.0.0", port=8000)

