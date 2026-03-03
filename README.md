This repository outlines the structure and code needed to connect an OPC UA-compatible PLC, such as the Siemens S7-1500 or S7-1200 to an OPC UA local client using the opcua library in python (opc_layer file).
Processing and packing into a JSON package and sending to a URL endpoint using https (processing_layer, transport_layer respectively)
Configurations for major components can be found in the config.py file.
Everything is finally run in the main.py file.
