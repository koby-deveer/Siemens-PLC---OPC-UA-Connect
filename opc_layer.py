from opcua import Client
import config

class OPCUAClientLayer:
    def __init__(self):
        self.client = Client(config.OPC_SERVER_URL)

        self.client.set_user(config.PLC_USERNAME)
        self.client.set_password(config.PLC_PASSWORD)

        self.client.set_security_string(
            f"Basic256Sha256,SignAndEncrypt,"
            f"{config.CLIENT_CERT_PATH},"
            f"{config.CLIENT_KEY_PATH}"
        )

        self.client.application_uri=config.APPLICATION_URI

    def connect(self):
        print("Connecting securely to PLC OPC UA server...")
        self.client.connect()
        print("Connected successfully.")

        self.tank1_node = self.client.get_node(config.TANK1_NODE_ID)
        self.tank2_node = self.client.get_node(config.TANK2_NODE_ID)

    def read_levels(self):
        tank1_value = self.tank1_node.get_value()
        tank2_value = self.tank2_node.get_value()
        return tank1_value, tank2_value

    def disconnect(self):
        self.client.disconnect()
