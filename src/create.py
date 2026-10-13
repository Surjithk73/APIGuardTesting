import httpx
BASE = "https://shipping.example.test"

def create_shipment(parcel, grams):
    """Business Intent: Preserve parcel identity and exact integer grams."""
    return httpx.post(f"{BASE}/shipments", json={"parcel": parcel, "grams": grams}).json()
