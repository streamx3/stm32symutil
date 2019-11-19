# stm32symutil
This program generates schematic symbols table for STM32 MCUs and CPUs.

![Preview](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/preview.png "Preview")

<br>

### Motivation:
Yes you can (and probably should) generate you footprint using Altium Footprint Wizard.

But:

1) Your MCU might be new, and there might be no symbols on resources like SnapEDA or Ultra Librarian.
2) Those existing ones might generate a tonn of clutter, look ugly and contain redundant non-native data when imported to Altium and even stay indexed as an additional library, despite the fact you only need them once. Not to mentoin bundled footprints sometimes have few pins misalligned.


Hence, "If you want something done right, do it yourself".

### How to use?
The implication is that you can generate a symbol table for preferred  MCU & package, and use Symbol Wizard in Altium, to create a beautiful native symbol in a jiffy.<br>
If you'te not aware of Altium Symbol Wizard and ability to make multipart symbols -- spend 5 minutes now, and save hours in future: https://www.youtube.com/watch?v=ceTr369zpDo <br>
You're welcome!

### How it works?
It takes data from STM32CubeMX or STM32CubeIDE, parses chip database and generates a spreadsheet.
For your convenience power pins can be mixed with GPIOs as they are located in chip, or separated into another table, so that you could conveniently copy each table into different Symbol Part in Altium symbol Wizard using Smart Copy (Ctrl + Shift + V or from context menu)

### Dependencies:
+ Python 3 https://www.python.org/downloads/
+ OpenPyXL. Install it with pip. On Ubuntu, you should probably use system package `python3-openpyxl`, on Windows -- open CMD with admin rights and use pip: `pip3 install openpyxl`


### TODO:
+ Validate Mac OS PATHs
+ Find reasonable block splitting model for STM32MP1, like NXP does

### Halp!
Open `cmd`, run `python stm32symgen.py -h`
```
stm32symgen.py --mcu MCU_name --af Alt_Func --power=Power_Align--outfile=OutFile
Details:
        --mcu [STM32F103C8Tx/STM32L552MEYxQ] -- you can type in both upper and
                lower case, ommit x and everything that goes after that,
                but onlyif anything after "x" is not ambiguous
        --af [all/none/first] or a list like adc,cec,dac,dcmi,ddr,debug,dfsdm,
                dsihost,eth,event,fdcan,fmc,fsmc,hdp,i2c,jtag,lcd,ltdc,quad,
                rcc,sai,sdmmc,spdif,spi,swd,sys,tamp,tim,trace,tsc,tsc,uart,
                usart,usb,wkup
        --af_split [y/n/yes/no] -- splits selected alternative functions
                in different columns
        --power_split [y/n/yes/no] -- if split selected, power pins will be put
                separately below, so they could be put into separate symbol
        --outfile [FILE] -- output filename for spreadsheet.
                If it's not ending with *.xlsx -- it'll be added for you.
        --help -- display this help
        --version -- displays program's version
        --mxpath [PATH] -- temporal path to CubeMX on Linux
        --idepath [PATH] -- temporal path to CubeIDE on Linux
Example:
         --mcu stm32f103cbt --power_split y -o 1.xlsx --af spi,i2c,uart,wkup,sys 
```

### Examples:
[Example 1](https://github.com/streamx3/stm32symutil/blob/master/examples/Example1.md "Example 1"): Basic example, with few alternative functions to display and a separate power part.

[Example 2](https://github.com/streamx3/stm32symutil/blob/master/examples/Example2.md "Example 2"): Minimal, no AF, 1 part

[Example 3](https://github.com/streamx3/stm32symutil/blob/master/examples/Example3.md "Example 3"): Minimal, but 2 parts

[Example 4-5](https://github.com/streamx3/stm32symutil/blob/master/examples/Example4-5.md "Example 4-5"): Using all the AFs

[Example 6](https://github.com/streamx3/stm32symutil/blob/master/examples/Example6.md "Example 6"): Huge MP1 CPU

<br>

Andrii Shelestov 2019

streamx3@gmail.com
