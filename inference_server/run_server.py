import uvicorn

if __name__ == "__main__":
    uvicorn.run("inference_server:app", host="0.0.0.0", port=10000, reload=True)
