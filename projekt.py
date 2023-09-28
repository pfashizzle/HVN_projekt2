import machine
import onewire
import ds18x20
import ujson
import utime

print("Hello")
# Läs konfigurationsfil
with open('config.json', 'r') as config_file:
    config = ujson.load(config_file)

# Konfigurera UART
# uart = machine.UART(config["uart_port"], baudrate=config["baud_rate"])

print(config["sensor_pin"])

# Skapa en OneWire-bus och DS18X20-sensor
ds_pin = machine.Pin(config["sensor_pin"])
ds_bus = onewire.OneWire(ds_pin)
ds_sensor = ds18x20.DS18X20(ds_bus)


while True:
    # Starta mätning
    ds_sensor.convert_temp()

    # Vänta på att mätningen ska bli klar
    utime.sleep_ms(750)

    # Läs temperaturen från sensorn
    temperature = ds_sensor.read_temp(ds_sensor.scan()[0])

    # Skicka temperaturen över UART
    #uart.write("Sensor ID: {}\nTemperature: {:.2f}°C\n".format(config["sensor_id"], temperature))
    print("Sensor ID: {}\nTemperature: {:.2f}°C\n".format(config["sensor_id"], temperature))


    # Vänta enligt mätningsintervallet
    utime.sleep(config["measurement_interval"])

