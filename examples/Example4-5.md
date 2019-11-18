### Example 4-5: Using all AFs in different ways

You can also generate all the AFs, but this is probably for analysis and printing plackards.
--af_split will cause each AF to have it's cell in Excell.

```
stm32symgen --mcu stm32f103tbu --power_split y -o stm32f103tbu_all.xlsx --af all
```

![Img 4](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_all.png "Img 4")


```
stm32symgen --mcu stm32f103tbu --power_split y -o stm32f103tbu_all_split.xlsx --af all --af_split y
```

![Img 5](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_all_split.png "Img 5")
