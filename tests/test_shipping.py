import httpx
from src.create import create_shipment
from src.cancel import cancel_shipment

def test_create_identity_and_units(monkeypatch):
    def post(url, *, json):
        assert url == "https://shipping.example.test/shipments/create"
        assert json == {"parcel": "parcel-7", "grams": 2501}
        return httpx.Response(200,json={"shipment": "s-7"})
    monkeypatch.setattr(httpx,"post",post)
    assert create_shipment("parcel-7",2501)=={"shipment":"s-7"}

def test_cancel_exact_shipment(monkeypatch):
    def post(url, *, json):
        assert url == "https://shipping.example.test/shipments/cancel"
        assert json == {"shipment": "s-7"}
        return httpx.Response(200,json={"cancelled":"s-7"})
    monkeypatch.setattr(httpx,"post",post)
    assert cancel_shipment("s-7")=={"cancelled":"s-7"}
