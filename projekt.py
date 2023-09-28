import machine
import onewire
import ds18x20
import ujson
import utime

print("Hello")
# Read configuration file
with open('config.json', 'r') as config_file:
    config = ujson.load(config_file)

# Create a OneWire bus
ds_bus = onewire.OneWire(machine.Pin(config["pin"]))

# Create a DS18X20 sensor for the bus
ds_sensor = ds18x20.DS18X20(ds_bus)

while True:
    # Scan for DS18B20 sensors on the bus
    sensor_ids = ds_sensor.scan()
    utime.sleep_ms(750)  # Adjust the sleep time based on your sensor's conversion time
    for sensor_id in sensor_ids:
        # Set the OneWire bus address to the current sensor's address
        ds_bus.addr = sensor_id

        # Start temperature measurement
        ds_sensor.convert_temp()

        # Wait for the measurement to complete
        utime.sleep_ms(750)  # Adjust the sleep time based on your sensor's conversion time

        # Read the temperature from the sensor
        temperature = ds_sensor.read_temp(sensor_id)

        # Convert the sensor_id bytearray to a readable hexadecimal string
        sensor_id_str = ''.join(['{:02X}'.format(byte) for byte in sensor_id])

        # Print the message in the specified format
        print("{} {} {:.2f}".format(sensor_id_str, sensor_id_str, temperature))
