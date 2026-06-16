import os

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    #return {"message": "Todo app"}
    return "<h1>Hello from Kubernetes!</h1>"


def main():
    port = int(os.getenv("PORT", "3000"))

    print(f"Server started in port {port}")

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
    )


if __name__ == "__main__":
    main()