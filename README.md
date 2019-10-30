# sensor-integration
Integration of Thermal Camera, Mic, Temperature and Gas Sensors with ubuntu.

The history.txt contains the list of all commands used by the previous engineer to get the sensors work in rpi3. 

## [Gas Sensor](https://www.digikey.com/product-detail/en/spec-sensors-llc/968-034/1684-1034-ND/6676880)

**Description**

As an initial development, the DGS-CO was chosen for measuring Carbon Monoxide. The DGS-CO is an electro-chemical sensor produced by the SPEC SENSORS company [28] for ambient monitoring purposes. It gives the calibrated and temperature-compensated CO gas value as well as Temperature and Relative Humidity values. The sensor uses the serial communication protocol over UART. Figure 26 illustrates the sensor and Table 4 shows its specifications. To acquire data, the sensor is easily connected to any microcontroller through its serial communication port. The connection parameters use 9600 baud and require 3.3V. To test the setup, here again the sensor data was acquired for a period of 40 minutes in the lab environment for both CO and relative humidity (RH). The plotted data is seen in Fig. 27. The gas value is given in parts-per-million (PPM).
**History**
11
​
12
'''
13
​
14
'''
