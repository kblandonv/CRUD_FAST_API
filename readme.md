# Two ways to run FastAPI
    1.  uvicorn main:app
    2.  Add lines of code
        if __name__ == "__main__":
            uvicorn.run("main:app", port=8000, reload=True)
        and run main.py