# ==============================
# PLC CONNECTION SETTINGS
# ==============================

OPC_SERVER_URL = "opc.tcp://192.168.0.1:4840"
APPLICATION_URI="urn:freeopcua:PythonOPC"

PLC_USERNAME = "OPC Client"
PLC_PASSWORD = "PLC@opc123"

CLIENT_CERT_PATH = "certs/client_cert.der"
CLIENT_KEY_PATH = "certs/client_key.pem"


TANK1_NODE_ID = "ns=3;s=T1_Val"
TANK2_NODE_ID = "ns=3;s=T2_Val"

# ==============================
# TANK CONFIGURATION
# ==============================

TANK1_CONFIG = {
    "tank_name": "Tank_1",
    "location": "North Yard",
    "capacity": "100000 ton",
    "min_level": 0,
    "max_level": 32,
    "low_alarm_threshold": 15,
    "high_alarm_threshold": 30,
    "unit": "feet"
}

TANK2_CONFIG = {
    "tank_name": "Tank_2",
    "location": "South Yard",
    "capacity": "100000 ton",
    "min_level": 0,
    "max_level": 32,
    "low_alarm_threshold": 15,
    "high_alarm_threshold": 30,
    "unit": "feet"
}

# ==============================
# CLOUD ENDPOINT
# ==============================

ENDPOINT_URL = "https://vgaohefsqkvxawapctlu.supabase.co/functions/v1/ingest-reading"
API_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZnYW9oZWZzcWt2eGF3YXBjdGx1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzE5MjkwNDAsImV4cCI6MjA4NzUwNTA0MH0.Xak71j_QvP4C1CC3XC49IYXujgS8qXDwWQ7ZamzsY9Q'

POLL_INTERVAL = 5  # seconds
