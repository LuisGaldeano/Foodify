#! /bin/sh

set -e
set -u
set -x

umask 000 # setting broad permissions to share log volume

# Start FastAPI application
uvicorn main:app --host "${FASTAPI_HOST}" --port "${FASTAPI_PORT}" --reload
