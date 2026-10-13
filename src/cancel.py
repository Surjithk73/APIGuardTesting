import httpx
BASE = "https://shipping.example.test"

def cancel_shipment(shipment):
    """Business Intent: Cancel exactly the requested shipment."""
    return httpx.post(f"{BASE}/shipments/cancel", json={"shipment": shipment}).json()
