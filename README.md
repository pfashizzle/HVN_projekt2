# Temperature Sensor Data Logger

This Python code project enables you to read temperature data from a DS18X20 temperature sensor and log it periodically using a MicroPython-compatible microcontroller. The temperature readings are printed to the console, and you can easily customize the code to send the data to other destinations.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yourusername/temperature-sensor-logger.svg)](https://github.com/yourusername/temperature-sensor-logger/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/temperature-sensor-logger.svg)](https://github.com/yourusername/temperature-sensor-logger/issues)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Hardware Setup](#hardware-setup)
  - [Uploading the Code](#uploading-the-code)
- [Configuration](#configuration)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)

## Prerequisites

Before using this code project, ensure you have the following:

1. A MicroPython-compatible microcontroller (e.g., ESP8266, ESP32).
2. A DS18X20 temperature sensor.
3. Proper wiring to connect the DS18X20 sensor to the microcontroller.

## Getting Started

### Hardware Setup

1. Connect the DS18X20 temperature sensor to your microcontroller as follows:
   - Data Pin (DS18X20) -> GPIO Pin (Microcontroller)
   - VCC (DS18X20) -> 3.3V (Microcontroller)
   - GND (DS18X20) -> GND (Microcontroller)

2. Make sure the connections are secure.

### Uploading the Code

1. Clone or download this code project to your local machine.

2. Transfer the code files to your MicroPython-compatible microcontroller using tools like ampy or webREPL.

3. Create a configuration file named `config.json` in the same directory as your code and configure it as explained in the [Configuration](#configuration) section below.

## Configuration

The code uses a configuration file named `config.json` to set up parameters. Create this file with the following structure:

{
    "sensor_pin": 12,              // GPIO pin to which the DS18X20 sensor is connected
    "sensor_id": "sensor_1",      // A unique identifier for your sensor
    "measurement_interval": 300   // Measurement interval in seconds
}

"sensor_pin": The GPIO pin to which the DS18X20 sensor is connected.
"sensor_id": A unique identifier for your sensor.
"measurement_interval": Measurement interval in seconds (e.g., 300 seconds for every 5 minutes).
Usage
To start logging temperature data, upload the code to your microcontroller and ensure it's running. The code will read temperature data from the DS18X20 sensor at the specified interval and print it to the console.

Customization
You can customize this code project to suit your needs:

Modify the code to send temperature data to a remote server or cloud service.
Implement data storage, visualization, or alerts based on your requirements.
Add additional sensors or sensors of different types.
Feel free to adapt and extend the code to fit your specific use case.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Oscar Åkerberg
GitHub: pfashizzle
Email: oscar.akerberg@live.se
Feel free to reach out if you have any questions or feedback.
