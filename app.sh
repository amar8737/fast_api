#!/usr/bin/env bash
set -e

source .venv/bin/activate
uvicorn storeapi.main:app --reloads