from asyncio import run as asyncio_run
import gateway_ble
import gateway_rest
from time import sleep

def main() -> None:
    
    # Getting values from BLE server
    temp, humidity = asyncio_run(gateway_ble.ble_server_mc_interface())
    
    post_status = gateway_rest.post_to_thingspeak(temp, humidity)
    print("Posted data to ThingSpeak with status code", post_status)
    sleep(8.0)

    actuation = 0
    actuation_rest = gateway_rest.get_from_thingspeak() 
    print("Actuation status received from ThingSpeak:", actuation_rest)
    if temp > 20 and humidity <50 and actuation_rest == None:
        actuation = 1
    elif actuation_rest != None:
        actuation = actuation_rest
    
    asyncio_run(gateway_ble.ble_actuator_mc_interface(actuation))

if __name__ == "__main__":
    main()
