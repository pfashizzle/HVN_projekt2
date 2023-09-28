import machine
import onewire
import ds18x20
import ujson
import utime

print("Hello")
# Read configuration file
with open('config.json', 'r') as config_file:
    config = ujson.load(config_file)

# Configure UART
# uart = machine.UART(config["uart_port"], baudrate=config["baud_rate"])

print(config["sensor_pin"])

# Create a OneWire bus and DS18X20 sensor
ds_pin = machine.Pin(config["sensor_pin"])
ds_bus = onewire.OneWire(ds_pin)
ds_sensor = ds18x20.DS18X20(ds_bus)

while True:
    # Start temperature measurement
    ds_sensor.convert_temp()

    # Wait for the measurement to complete
    utime.sleep_ms(900)

    # Read the temperature from the sensor
    temperature = ds_sensor.read_temp(ds_sensor.scan()[0])

    # Send the temperature over UART
    # uart.write("Sensor ID: {}\nTemperature: {:.2f}°C\n".format(config["sensor_id"], temperature))
    print("Sensor ID: {}\nTemperature: {:.2f}°C\n".format(config["sensor_id"], temperature))

    # Wait according to the measurement interval
    # utime.sleep(config["measurement_interval"])