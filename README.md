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

To see if the serial port is connceted use `sudo dmesg | grep tty`. You should get something like this:
```
[    0.000000] Kernel command line: 8250.nr_uarts=1 bcm2708_fb.fbwidth=1920 bcm2708_fb.fbheight=1200 bcm2708_fb.fbswap=1 vc_mem.mem_base=0x3ec00000 vc_mem.mem_size=0x40000000  dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p7 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait splash plymouth.ignore-serial-consoles
[    0.000812] console [tty1] enabled
[    1.043347] 3f201000.serial: ttyAMA0 at MMIO 0x3f201000 (irq = 87, base_baud = 0) is a PL011 rev2
[    1.053751] 3f215040.serial: ttyS0 at MMIO 0x0 (irq = 166, base_baud = 50000000) is a 16550
```




## [Temperature Sensor]()

**Description**

## [Microphone]()

**Description**

## [Thermal Camera]()

**Description**
