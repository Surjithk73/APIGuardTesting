import httpx
BASE = "https://shipping.example.test"

def cancel_shipment(shipment):
    """Business Intent: Cancel exactly the requested shipment."""
    return httpx.post(f"{BASE}/cancel", json={"shipment": shipment}).json()
