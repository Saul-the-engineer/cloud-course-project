"""Create a FastAPI app."""

import os

from fastapi import FastAPI

from files_api.routes import ROUTER


def create_app(s3_bucket_name: str = None) -> FastAPI:
    """Create a FastAPI app."""
    s3_bucket_name = s3_bucket_name or os.getenv("S3_BUCKET_NAME")
    app = FastAPI()
    app.state.s3_bucket_name = s3_bucket_name
    app.include_router(ROUTER)
    return app


if __name__ == "__main__":
    import uvicorn

    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
