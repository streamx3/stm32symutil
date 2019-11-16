# stm32symutil
This program generates a schematic symbol table from STM32 MCUs and CPUs.

### Motivation:
1) Your MCU might be new, and there might be no symbols on resources like SnapEDA or Ultra Librarian.
2) Those existing ones might generate a tonn clutter, look ugly and contain redundant non-native data, when imported to Altium. Not to mentoin bundled footprints that sometimes have few pins misalligned.
Hence, "If you want something done right, do it yourself".

### What it does?
The implication is that you can generate a symbol table for preferred  MCU & package, and use Symbol Wizard in Altium, to create a beautiful native symbol in a jiffy.<br>
If you'te not aware of Altium Symbol Wizard and ability to make multipart symbols -- spend 5 minutes now, and save hours in future. You're welcome!

### How it works?
It takes data from STM32CubeMX or STM32CubeIDE, parses chip database and generates a spreadsheet.
For your convenience power pins can be mixed with GPIO as they go in chip, or separated into another table so that you could conveniently copy each table into different Symbol Part in Altium symbol Wizard using Smart Copy (Ctrl + Shift + V or from context menu)

### Dependencies:
+ Python 3 https://www.python.org/downloads/
+ OpenPyXL. Install it with pip. On Ubuntu, you should probably use system package `python3-openpyxl`, on Windows -- open CMD with admin rights and use pip: `pip3 install openpyxl`


### TODO:
-- Validate Mac OS PATHs
-- Find reasonable block splitting model for STM32MP1, like NXP does

### Halp!
Open `cmd`, run `python stm32symgen.py`
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

### Example 1:
The simplest way to run an app
```
stm32symgen --mcu stm32f103tbu -o stm32f103tbu_none.xlsx --af none
```
![Img 1](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_unsplit.png "Img 1: Unsorted power pins, no Alternative functions")
![Img 2](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_unsplit_sym.png "Img 2: Unsorted power pins, no Alternative functions, SYM")


### Example :
The simplest way to run an app

```
stm32symgen --mcu stm32f103tbu --power_split y -o stm32f103tbu_all_split.xlsx --af all --af_split y
```
![Img 12](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_all.png "Img 2: ")
![Img 13](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_all_split.png "Img 3: ")

### Example :
![Img 14](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_basic.png "Img 4: ")
![Img 15](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_basic_p1.png "Img 5: ")
![Img 16](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none.png "Img 6: ")
![Img 17](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_p1.png "Img 7: ")
![Img 18](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_p2.png "Img 8: ")
Remove https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_sym.png

### Example N:
Most complex example with MP1 CPU.
```
stm32symgen --mcu stm32mp157cad --power_split y -o stm32mp157cad.xlsx --af spi,i2c,uart,sys,wkup,debug,ddr,usb
```
Output table:

![Img 111](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stmp32mp1.png "Img 11: ")
Symbol, part 1:

![Img 112](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stmp32mp1_p1.png "Img 12: ")
Symbol, part 2:

![Img 113](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stmp32mp1_p2.png "Img 13: ")


```
stm32symgen --mcu stm32f103tbu --power_split y -o stm32f103tbu_none.xlsx --af none
```

```
stm32symgen --mcu stm32f103tbu --power_split y -o stm32f103tbu_basic.xlsx --af spi,i2c,uart,sys,wkup
```

```
stm32symgen --mcu stm32f103tbu --power_split y -o stm32f103tbu_all.xlsx --af all
```




Andrii Shelestov 2019
streamx3@gmail.com
