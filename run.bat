@echo off
set DEFAULT_PORT=8000

pip install -r requirements.txt

if "%1"=="" (
    uvicorn app.main:app --port %DEFAULT_PORT% --reload
) else (
    uvicorn app.main:app --port %1 --reload
)
