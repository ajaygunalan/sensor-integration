# Sensor-integration
Integration of Thermal Camera, Mic, Temperature and Gas Sensors with ubuntu.

The history.txt contains the list of all commands used by the previous engineer to get the sensors work in rpi3. 

## To Do

1. Integrate with RPI3 to see if sensors work properly and also to understand about the interface.
2. Then Integrate with Nvidia Jeston Xavier.

## [Gas Sensor](https://www.digikey.com/product-detail/en/spec-sensors-llc/968-034/1684-1034-ND/6676880)

**Description**

As an initial development, the DGS-CO was chosen for measuring Carbon Monoxide. The DGS-CO is an electro-chemical sensor produced by the SPEC SENSORS company for ambient monitoring purposes. It gives the calibrated and temperature-compensated CO gas value as well as Temperature and Relative Humidity values. The sensor uses the serial communication protocol over UART. To acquire data, the sensor is easily connected to any microcontroller through its serial communication port. The connection parameters use 9600 baud and require 3.3V.

* [Connection Diagram](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_to_rpi.png)
* [Sample Code](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_sensor/pic/sample_code_for_algo.png)



## [Temperature Sensor]()

**Description**

## [Microphone]()

**Description**

## [Thermal Camera]()

**Description**
