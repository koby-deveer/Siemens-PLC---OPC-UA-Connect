import config
from processing_layer import ProcessingLayer
from transport_layer import TransportLayer

while True:
    tank1_level=20
    tank2_level=20

    tank1_payload = ProcessingLayer.build_tank_data(
                    tank1_level,
                    config.TANK1_CONFIG
                )

    tank2_payload = ProcessingLayer.build_tank_data(
                    tank2_level,
                    config.TANK2_CONFIG
                )

    TransportLayer.send_payload(tank1_payload)
    TransportLayer.send_payload(tank2_payload)