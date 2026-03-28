# api/main.py
"""
FinCA – FastAPI Backend Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FinCA API",
    description="Multi-Agent Generative AI for CA Task Automation",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to FinCA API", "version": "0.1.0", "status": "development"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# TODO: Add routers
# from api.routes import tax, gst, audit, compliance, advisory
# app.include_router(tax.router, prefix="/tax", tags=["Tax"])
# app.include_router(gst.router, prefix="/gst", tags=["GST"])
# app.include_router(audit.router, prefix="/audit", tags=["Audit"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
