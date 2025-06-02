from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database.database import engine, Base
from .api import students, courses, enrollments

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="RegMatriculasPy",
    description="Sistema de registro de matrículas estudiantiles",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(students.router, prefix="/api/students", tags=["students"])
app.include_router(courses.router, prefix="/api/courses", tags=["courses"])
app.include_router(enrollments.router, prefix="/api/enrollments", tags=["enrollments"])

@app.get("/")
async def root():
    return {"message": "Welcome to RegMatriculasPy API"}
