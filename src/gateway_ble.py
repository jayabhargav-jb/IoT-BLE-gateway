import asyncio
import bleak
from time import sleep
import requests

async def ble_server_mc_interface() -> tuple:
    devices = await bleak.BleakScanner.discover()
    for device in devices:
        if device.name == 'Sensor Node BLE400':
            print('Found device:', device.address)
            break

    client = bleak.BleakClient(device.address, timeout=20)
    await client.connect()
    services = client.services 

    a = await client.read_gatt_char("CCC1")
    print("Temperature value received:", a[0])
    b = await client.read_gatt_char("DDD1")
    print("Humidity value received:", b[0])

    await client.disconnect()

    return a[0], b[0]

async def ble_actuator_mc_interface(actuation:int) -> None:
    devices = await bleak.BleakScanner.discover()
    for device in devices:
        if device.name == 'Actuator Node BLE400':
            print('Found device:', device.name)
            break

    client = bleak.BleakClient(device.address, timeout=20)
    await client.connect()
    services = client.services
    # actuation.to_bytes()
    await client.write_gatt_char("EEE1", actuation.to_bytes())
    print("Actuation Successful, disconnecting from device.")
    await client.disconnect()

if __name__ == "__main__":
    a, b = asyncio.run(ble_server_mc_interface())
    asyncio.run(ble_actuator_mc_interface(0))



