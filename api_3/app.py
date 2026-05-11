from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# Enable CORS so your HTML file can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
async def get_products():
    # This matches the structure expected by the JavaScript fetch function
    return [
        {
            "name": "Docker Container Pro",
            "price": 49.99,
            "description": "High-performance container optimized for scale.",
            "image_url": "https://img.icons8.com/color/144/docker.png"
        },
        {
            "name": "Kubernetes Orchestrator",
            "price": 89.99,
            "description": "The ultimate tool for managing container clusters.",
            "image_url": "https://img.icons8.com/color/144/kubernetes.png"
        },
        {
            "name": "Jenkins CI Pipeline",
            "price": 29.99,
            "description": "Automate your builds with this pre-configured image.",
            "image_url": "https://img.icons8.com/color/144/jenkins.png"
        }
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)