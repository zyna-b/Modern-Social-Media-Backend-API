from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import os

# from app import models
# from .database import engine
from .routers import post, user, auth, vote


# Create database tables
# We dont need this for now as we setup Alembic, which is a data migration tool
# Uncomment the line below if you want to create tables directly without migrations

# models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="SocialFeed API",
    description="A modern social media backend API",
    version="1.0.0"
)

origins = ["*"]  # Allow all origins during development

# For production, you might want to restrict origins
# if os.getenv("ENVIRONMENT") == "production":
#     origins = [
#         "https://your-frontend-app.onrender.com",
#         "https://your-domain.com"
#     ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# Root endpoint
@app.get("/")
def get_user():
    return {"message": "Hello, Zainab!"}

# Health check endpoint (required by many platforms including Render)
@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

    

# To run the app, use the command: uvicorn app.main:app --reload

