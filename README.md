# Temperature Sensor Data Logger

This MicroPython code project allows you to read temperature data from DS18B20 or DS18X20  temperature sensors using a microcontroller. The code scans for sensors on the OneWire bus, measures temperatures, and prints the readings to the console. You can adapt and extend this code to suit your specific needs.


[![GitHub stars](https://img.shields.io/github/stars/pfashizzle/HVN_projekt2.svg)](https://github.com/pfashizzle/HVN_projekt2/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/pfashizzle/HVN_projekt2.svg)](https://github.com/pfashizzle/HVN_projekt2/issues)



## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Hardware Setup](#hardware-setup)
- [Uploading the Code](#uploading-the-code)
- [Configuration](#configuration)
- [Usage](#usage)

## Prerequisites

Before using this code project, ensure you have the following prerequisites:

1. Suitable microcontroller ( I used a raspberry pico ).
2. One or more DS18B20/DS18X20 temperature sensors.
3. Wiring to connect the DS18B20/DS18X20 sensor(s) to the microcontroller.

## Getting Started

### Hardware Setup

1. Connect the DS18B20 temperature sensor(s) to your microcontroller as follows:
   - Data Pin (DS18B20/DS18X20) -> GPIO Pin (Microcontroller)
   - VCC (DS18B20/DS18X20) -> 3.3V (Microcontroller)
   - GND (DS18B20/DS18X20) -> GND (Microcontroller)

2. Ensure the connections are secure.

### Uploading the Code

1. Clone or download this code project to your local machine.

2. Transfer the code files to your microcontroller.

3. Create a configuration file named `config.json` in the same directory as your code and configure it as explained in the [Configuration](#configuration) section below.

## Configuration

The code uses a configuration file named `config.json` to set up parameters. Create this file with the following structure:

json:
{
   
   "pin": 16,
   
   "measurement_interval": 900
   
}

"pin": The GPIO pin to which the DS18B20/DS18X20 sensor(s) are connected.


"measurement_interval": Measurement interval in milliseconds (e.g., 3000 milliseconds for every 3 seconds).

Usage
To start reading temperature data, upload the code to your microcontroller and ensure it's running. The code will scan for DS18B20/DS18X20 sensors on the OneWire bus, measure temperatures, and print the readings to the console.

Customization
You can customize this code project to suit your needs:

Modify the code to send temperature data to a remote server or cloud service.
Implement data storage, visualization, or alerts based on your requirements.
Add additional sensors or sensors of different types.
Feel free to adapt and extend the code to fit your specific use case.

*************************************************************************************
Author

Oscar Åkerberg

GitHub: pfashizzle

Email: oscar.akerberg@live.se

*************************************************************************************
