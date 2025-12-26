from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from app.routes import upload
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title='DU-Maps',
    description='AI-powered document and book analysis',
    version='1.0.0'
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload.router,prefix="/api")