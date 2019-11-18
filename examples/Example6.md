### Example 6: Minimalistic

Most complex example with MP1 CPU.
```
stm32symgen --mcu stm32mp157cad --power_split y -o stm32mp157cad.xlsx --af spi,i2c,uart,sys,wkup,debug,ddr,usb
```
Output table:

![Img 6.1](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stmp32mp1.png "Img 6.1")

Symbol, part 1:

![Img 6.2](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stmp32mp1_p1.png "Img 6.2")

Symbol, part 2:

![Img 6.3](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stmp32mp1_p2.png "Img 6.2")
