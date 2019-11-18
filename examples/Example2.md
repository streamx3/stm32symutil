### Example 2: Minimalistic

If you want a small symbol with no extra info and power pins in one part -- do the following:

```
stm32symgen --mcu stm32f103tbu --power_split n -o stm32f103tbu_none.xlsx --af none
```

It will look like this:

![Img 2.1](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_unsplit.png "Img 2.1: Unsorted power pins, no Alternative functions")

![Img 2.2](https://raw.githubusercontent.com/streamx3/stm32symutil/master/images/stm32f103tbu_none_unsplit_sym.png "Img 2.2: Unsorted power pins, no Alternative functions, SYM")
