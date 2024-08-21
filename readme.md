# deej on a Raspberry Pi Pico
> (**avalible on:** `Raspberry Pi Pico`, `Raspberry Pi Pico W`, `Raspberry Pi Pico 2` (`Raspberry Pi Pico H`, `Raspberry Pi Pico WH`) )
> 
> ---
> 
> requirements:
> - **`circuitpython`** must be the os for the rpi-pico
> - **`1-3 potentiometers`** \
`5 kOhm` or `10 kOhm` or `100 kOhm` \
may be anything in between `5 kOhm` to `100 kOhm` \
(`100 kOhm` is \*best\*, _larger than 100kOhm is **too high**_) \
should be `linear potentiometers`
> 
> ---
> 
> specifications:
> - **`up to 3 potentiometers`**
> - **`scan rate: 50ms (default) (adjustable)`**
> 
> ---


> ## How to install
> 
>>1. - **install circuitpython** on the rpi-pico
>>>>>> - **`How?`**  read the [CircuitPython Quickstart](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython) __or__ `install circuitpython` with **`thonny`**
>>2. - **copy** `boot.py` and `code.py` onto the rpi-pico
>> 
>> **done** *(on the software side)*
>>
>> ---
> 
> 
> 


> ## How to stop the device when it is running or no longer responding correctly
>>
>> **option 1**
>>> to stop the rpi at any time you can connect **`GND`** and **`GP17`**.
>>> This will **force** the main-loop to stop and deinit all the analog pin instances.
>>
>> **option 2**
>>> simply unplug the device from your pc and reconnect it



> ## installing circuitpython on a raspberry pi pico
>
>> 1. dowload the `.uf2` file from [`here`](https://circuitpython.org/board/raspberry_pi_pico/).\
>> 2. then disconnect the rpi-pico from your PC.\
>> 3. hold the `BOOTSEL` button while you connect it with a USB cable (USB data cable) to your PC, untill you see it pop up as a USB-storage device.\
>> 4. now you can stop holding the `BOOTSEL` button.\
>> 5. if there is a file named `INFO_UF2.TXT` on the rpi-pico, you have successfully booted into the `BOOTSEL` mode.\
>> 6. just copy the `.UF2` to directly onto the 
