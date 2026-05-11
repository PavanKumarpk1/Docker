from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS so the Frontend UI can fetch data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def get_products():
    return [
        {"name": "Storage Node", "price": 25, "image_url": "https://img.icons8.com/color/144/database.png"},
        {"name": "Compute Unit", "price": 50, "image_url": "https://img.icons8.com/color/144/cpu.png"},
        {"name": "Network Bridge", "price": 15, "image_url": "https://img.icons8.com/color/144/router.png"}
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
