### Example 1: Basic

Thet's the way I think you should use it:
+ Pick an MCU
+ Set output file
+ Select few alternative functions you want to see
+ Power pins will be separated by default

```
stm32symgen --mcu stm32f103tbu -o stm32f103tbu_basic.xlsx --af spi,i2c,uart,sys,wkup
```

It will look like this:
![Img 1.1](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_basic.png "Img 1.1: ")

Copy 2 separate tables to Symbol Wizard in Altium and create 2 parts:
![Img 1.2](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_basic_p1.png "Img 1.2: ")
<br>
![Img 1.3](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_basic_p1.png "Img 1.3: ")
