import time
import config
from opc_layer import OPCUAClientLayer
from processing_layer import ProcessingLayer
from transport_layer import TransportLayer


def main():

    opc_client = OPCUAClientLayer()
    opc_client.connect()

    while True:
        try:
            tank1_level, tank2_level = opc_client.read_levels()

            tank1_payload = ProcessingLayer.build_tank_data(
                tank1_level,
                config.TANK1_CONFIG
            )

            tank2_payload = ProcessingLayer.build_tank_data(
                tank2_level,
                config.TANK2_CONFIG
            )

            print(tank1_payload)
            print(tank2_payload)
            
        except Exception as e:
            print("Error occurred:", e)
            print("Attempting reconnect...")
            opc_client.disconnect()
            time.sleep(5)
            opc_client.connect()

        time.sleep(config.POLL_INTERVAL)


if __name__ == "__main__":
    main()
