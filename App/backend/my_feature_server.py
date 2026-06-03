import os
import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

app = FastAPI()

DIRECTORY = "."

def log_lead(destination, service_type):
    file_path = os.path.join(DIRECTORY, "leads.txt")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"[{timestamp}] Destination: {destination}, Service: {service_type}\n")

@app.get("/track")
def track(destination: str, service_type: str):
    log_lead(destination, service_type)
    
    # Real partner routing numbers
    partners = {
        "car_hire": "https://wa.me/254758378722",
        "flight": "https://wa.me/254758378722",
        "hotel": "https://wa.me/254758378722"
    }
    
    # Redirect to the matched number, or fallback to the main number
    return RedirectResponse(partners.get(service_type, "https://wa.me/254758378722"))

if __name__ == "__main__":
    print("Starting production tracking server on port 10000...")
    uvicorn.run(app, host="0.0.0.0", port=10000)
