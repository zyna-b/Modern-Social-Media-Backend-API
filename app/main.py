from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

# from app import models
# from .database import engine
from .routers import post, user, auth, vote


# Create database tables
# We dont need this for now as we setup Alembic, which is a data migration tool
# Uncomment the line below if you want to create tables directly without migrations

# models.Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI()

origins = ["*"]  # Allow all origins during development

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

# request Get method url: "/"
@app.get("/")
def get_user():
    return {"message": "Hello, Zainab!"}

    

# To run the app, use the command: uvicorn app.main:app --reload

