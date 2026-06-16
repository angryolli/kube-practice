import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Todo app"}


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