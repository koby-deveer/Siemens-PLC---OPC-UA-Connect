import requests
import config

class TransportLayer:

    @staticmethod
    def send_payload(payload):

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {config.API_TOKEN}"
        }

        response = requests.post(
            config.ENDPOINT_URL,
            json=payload,
            headers=headers,
            timeout=10
        )

        print("Sent:", payload["tank_name"],
              "| Status:", response.status_code)
