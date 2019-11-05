# Sensor-integration
Integration of Thermal Camera, Mic, Temperature and Gas Sensors with ubuntu.

The [history.txt](https://github.com/ajaygunalan/sensor-integration/blob/master/history.txt) contains the list of all commands used by the previous engineer to get the sensors work in rpi3. 

## Contents

1. [Gas Sensor](#gas-sensor)
2. [Temperature Sensor](#temperature-sensor)
3. [Microphone](#microphone)
4. [Thermal Camera](#thermal-camera)


## To Do

1. Integrate with RPI3 to see if sensors work properly and also to understand about the interface.
2. Then Integrate with Nvidia Jeston Xavier.

## [Gas Sensor](https://www.digikey.com/product-detail/en/spec-sensors-llc/968-034/1684-1034-ND/6676880)

**Description**

As an initial development, the DGS-CO was chosen for measuring Carbon Monoxide. The DGS-CO is an electro-chemical sensor produced by the SPEC SENSORS company for ambient monitoring purposes. It gives the calibrated and temperature-compensated CO gas value as well as Temperature and Relative Humidity values. The sensor uses the serial communication protocol over UART. To acquire data, the sensor is easily connected to any microcontroller through its serial communication port. The connection parameters use **9600 baud** and require **3.3V**.

* [Connection Diagram](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_to_rpi.png)
* [Sample Code](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_sensor/pic/sample_code_for_algo.png)
* [To configure UART](https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c)
* [Code which works in rpi3](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_sensor/pic/serial_read2.py)



## [Temperature Sensor](https://www.adafruit.com/product/381)


**Description**

There are four types of sensors for measuring the ambient temperature: 
(i) Negative Temperature Coefficient (NTC)
(ii) Resistance Temperature Detector (RTD)
(iii) Thermocouple
(iv) Semiconductor-based sensors.

Considering the project requirements, DS18B20 waterproof digital temperature sensor from Adafruit was selected, which is a semiconductor-based sensor. The 1-wire technology uses the serial protocol with a single communication line. A 1-Wire master
initiates and controls the communication with one or more 1-Wire slave devices on the 1-Wire bus.

Each 1-Wire slave device has a unique, unalterable, factory-programmed, 64-bit ID, which serves as device address on the 1-Wire bus. We can connect as many DS18B20 sensors as we need in parallel.

As per the sensor datasheet, it takes 750 ms for the sensor reading. Therefore, a 1 Hz
frequency of reading for this sensor was chosen. This should not be a problem since temperature itself
is a slow variable and does not change very fast.

Connections, If your sensor has three wires:

* Red to 3-5V 
* Blue to ground
* Yellow to GPIO(data)

* [Code which works in rpi3](https://github.com/ajaygunalan/sensor-integration/blob/master/thermometer.py)

**Reference**
* [youtube video](https://www.youtube.com/watch?v=SHOO7wIRVCs)

## [Microphone]()

**Description**

Humans usually utilize sound source localization, separation, and identification enabling them to
operate properly in hazardous environments. However, in robotic teleoperation, without the
human being present in the environment, this sound information may not be communicated as is to
the operator who remotely controls the robot. Communicating the different sound-based
environmental feedback to the operator can give them more perception of the field more effectively.

Being aware of the surrounding sound activity can allow the operator to plan the next steps in the
operation, avoid dangers, detect human activity, etc.

In this project, having this acoustic information can be very helpful. Not only can it help to find potential
survivors in disaster scenarios, but also help the operators to localize different sounds in the
environment. For instance, explosions, gas leaks, building collapses, etc., can be detected by the
operator, which will be highly beneficial to improve search-n-rescue tasks both in terms of time and
efficiency.

The [XCORE-200 XUF216 microphone array by XMOS](https://www.xmos.com/products/voice/micarray) was selected
for this task. It provides audio capture from microphones arranged along the circumference of the
device, which has a 90 mm diameter. Each captured input is converted into a modulated audio stream
and transferred to the host processor through a high-speed USB connection. The system can be
configured to generate output at **sample rates from 7.35 kHz to 48 kHz.** It is comprised of **seven
INFINEON IM69D130 microphones, which have embedded fast and low-noise analog-to-digital
convertors.**

The device includes an eight-channel decimator, programmable output sample rate between (8, 12,
16, 24, or 48 kHz), up to 100 dB dynamic range with gain compensation, and a delay resolution up to
2.6 us (384 kHz).

To acquire data from the microphone array and analyse its behaviour, the [ManyEars](https://sourceforge.net/p/manyears/wiki/Main_Page/), a Open Framework
is an open source software prevalent for robotic applications. The framework provides sound
source localization, tracking, separation, as well as post-filtering. 

The [ODAS (Open Embedded Audition System)](https://github.com/introlab/odas) library is a software package, which uses the ManyEars framework at its core and builds a user interface to test the different algorithms for sound analysis. For the initial testing of the device, the ODAS library was used. ODAS is coded entirely in C for easy portability, and is optimized to run on low-cost embedded hardware. It is free and open source. ODAS Studio is a desktop interface that
visually represents the data acquired by the ODAS algorithm and manages the recordings of separated
audio sources. The audio energy and tracked audio sources are represented on a unit sphere. 

In this mode, the overall direction of the tracked sound source can be localized.

For transmission of the acoustic data to the MASTER station, here again a Linux-based solution was
adopted. The acquired microphone digital data is transmitted to a processing unit. The processing unit
implements the ODAS library and performs data processing in three steps: 

(i) Data pre-processing – using the MicST (Microphone Signal Transform) data structure to transform the time-domain
signal of each microphone (sampled at 48,000 samples/sec) in weighted frequency frames. Further,
the MCRA (Minimum Controlled Recursive Averaging) function estimates the spectrum of the
stationary noise during silence periods, so as to subtract it during processing; 

(ii) Localization – to localize up to four different sound sources using Beam-forming algorithm; and 

(iii) Tracking – the detected sound source using particle filter. This information is then transmitted to the master station
through the UDP packets and finally represented in the VR environment. It is worth mentioning that
all of the UDP packets are organized in JSON standard in order to have the unique shape.

**To Get Data from the Mic**

1. Install odas, follow the steps [here](https://github.com/introlab/odas/wiki/installation).
2. Then [install odas web](https://github.com/introlab/odas_web)
3. Go to odas web directory and run `npm start`
4. In another terminal, go to `/odas/bin` and then make sure to have [this config file.](https://github.com/ajaygunalan/sensor-integration/blob/master/myConfigFile_OK.cfg)
5. Now, run `./odaslive -c myConfigFile_OK.cfg -v`




## [Thermal Camera]()

**Description**

Thermal imaging camera is a device that forms an image using infrared radiation in the **14000 nm**
wavelength range. Having a thermal imaging camera can enable the operator to see the distribution
of the temperature in an environment, the hot or cold places in the environment. This can, in turn, be used to
identify very hot areas or recognize gas leaks, living beings, etc. In this sense, thermal imaging can provide additional information that is not readily available to the naked eye.

There are various types of the thermal cameras available with different specifications
in terms of sensor size, frame rate, etc. [FLIR’s C3 thermal camera](https://www.flir.com/products/c3/)  was chosen
based on the constraints of desired quality vs.
weight and cost. 

It comes recommended for inspections within buildings and facilities, which lends itself very
well with the use-cases identified for this project.

Moreover, the camera has a live video streaming over USB as well as wifi. The image shows the overall distribution of temperature in the field-ofview through colour. The cursor can be used to pinpoint the temperature at a particular location.

The limitation is that the sensor needs to be calibrated or held on a particular view for a few seconds
before the temperature stabilizes. Additionally, the depth information of a particular location is not
available. Therefore, the thermal image needs to be used in combination with other information from
the environment to make sense of the data.

For transmission of the thermal camera video to the MASTER station, a Linux-based solution was
adopted. The OpenCV library is well suited to acquire and transmit the image with optimal latency,
frequency, and image quality.The video stream is acquired through OpenCV’s input function and encoded into the jpeg format
to reduce bandwidth. After that, the encoded frame is sent over a UDP socket to the master station
and it is finally shown in the VRE. Based on preliminary experiments, this method allows a transmission
frequency up to 69 frames-per-second.

