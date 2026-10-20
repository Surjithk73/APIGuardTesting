"""Theatre V1 adapter. APIShield updates this source when its contract changes."""
import os
import httpx

THEATRE_URL = os.environ.get('CINEMA_THEATRE_URL', 'http://127.0.0.1:8101')


class TheatreClient:
    def __init__(self, client=None):
        self.client = client or httpx.Client(base_url=THEATRE_URL, timeout=10, trust_env=False)

    def list_shows(self):
        response = self.client.get('/shows')
        response.raise_for_status()
        return response.json()['shows']

    def get_seats(self, show_id):
        response = self.client.get(f'/shows/{show_id}/seats')
        response.raise_for_status()
        data = response.json()
        if 'availability' in data:
            return data['availability']['seats']
        return data['seats']

    def hold_seats(self, show_id, seat_ids, idempotency_key):
        response = self.client.post('/holds', json={'show_id': show_id, 'seat_ids': seat_ids, 'idempotency_key': idempotency_key})
        response.raise_for_status()
        data = response.json()
        if 'hold' in data:
            hold = data['hold']
            return {
                'hold_id': hold['id'],
                'amount_paise': hold['total']['value'],
                'expires_at': hold['expires_at'],
                **data,
            }
        return data

    def confirm_booking(self, hold_id, payment_id):
        response = self.client.post('/bookings', json={'confirmation': {'hold_id': hold_id, 'payment_id': payment_id}})
        response.raise_for_status()
        return response.json()
