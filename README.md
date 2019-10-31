# Sensor-integration
Integration of Thermal Camera, Mic, Temperature and Gas Sensors with ubuntu.

The [history.txt](https://github.com/ajaygunalan/sensor-integration/blob/master/history.txt) contains the list of all commands used by the previous engineer to get the sensors work in rpi3. 

## To Do

1. Integrate with RPI3 to see if sensors work properly and also to understand about the interface.
2. Then Integrate with Nvidia Jeston Xavier.

## [Gas Sensor](https://www.digikey.com/product-detail/en/spec-sensors-llc/968-034/1684-1034-ND/6676880)

**Description**

As an initial development, the DGS-CO was chosen for measuring Carbon Monoxide. The DGS-CO is an electro-chemical sensor produced by the SPEC SENSORS company for ambient monitoring purposes. It gives the calibrated and temperature-compensated CO gas value as well as Temperature and Relative Humidity values. The sensor uses the serial communication protocol over UART. To acquire data, the sensor is easily connected to any microcontroller through its serial communication port. The connection parameters use 9600 baud and require 3.3V.

* [Connection Diagram](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_to_rpi.png)
* [Sample Code](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_sensor/pic/sample_code_for_algo.png)
* [To configure UART](https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c)
* [Code which works in rpi3](https://github.com/ajaygunalan/sensor-integration/blob/master/gas_sensor/pic/serial_read2.py)



## [Temperature Sensor]()

**Description**

## [Microphone]()

**Description**

**Requirments:**

Humans usually utilize sound source localization, separation, and identification enabling them to
operate properly in hazardous environments [29]. However, in robotic teleoperation, without the
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

(i) Data pre-processing – using the MicST (Microphone Signal Transform, [31]) data structure to transform the time-domain
signal of each microphone (sampled at 48,000 samples/sec) in weighted frequency frames. Further,
the MCRA (Minimum Controlled Recursive Averaging) function estimates the spectrum of the
stationary noise during silence periods [33], so as to subtract it during processing; 

(ii) Localization – to localize up to four different sound sources using Beam-forming algorithm; and 

(iii) Tracking – the detected sound source using particle filter. This information is then transmitted to the master station
through the UDP packets and finally represented in the VR environment. It is worth mentioning that
all of the UDP packets are organized in JSON standard in order to have the unique shape. Figure 30
shows the overall block diagram of the acoustic data transmission. 

## [Thermal Camera]()

**Description**
