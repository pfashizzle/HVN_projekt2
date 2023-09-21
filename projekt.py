import machine
import onewire
import ds18x20
import ujson
import utime

# Konfigurera DS18B20-sensor
ow = onewire.OneWire(machine.Pin(4))  # Anslut DS18B20 till GPIO-pin 4
temp_sensor = ds18x20.DS18X20(ow)

# Konfigurera UART-kommunikation
uart = machine.UART(0, baudrate=9600, tx=machine.Pin(0), rx=machine.Pin(1))

# Läs av och skicka temperaturdata regelbundet
while True:
    temp_sensor.convert_temp()
    utime.sleep_ms(750)  # Vänta på att mätningen ska bli klar

    # Läs av temperaturvärdet
    roms = temp_sensor.scan()
    for rom in roms:
        temperature = temp_sensor.read_temp(rom)

        # Skapa ett JSON-objekt med temperaturdata
        data = {
            "device": "pico",
            "temperature": temperature,
            "timestamp": utime.time()
        }
        json_data = ujson.dumps(data)

        # Skicka data över UART
        uart.write(json_data + "\n")
        
        utime.sleep(10)  # Vänta i 10 sekunder innan nästa avläsning