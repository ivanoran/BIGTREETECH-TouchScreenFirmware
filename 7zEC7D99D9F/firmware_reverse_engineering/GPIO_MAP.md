# GPIO_MAP — используемые выводы (образ B), восстановлено из вызовов `GPIO_Init` (0x08011112)

Структура `GPIO_InitTypeDef` в этом бинарнике: `{u16 pin @0; u8 speed @2; u8 mode @3}` (0x08011114–0x08011158: `ldrb [r1,#3]` = mode, `ldrb [r1,#2]` = speed). Коды режима SPL: 0x00 AIN, 0x04 IN_FLOATING, 0x28 IPD, 0x48 IPU, 0x10 OUT_PP, 0x14 OUT_OD, 0x18 AF_PP, 0x1C AF_OD. Скорость 3 = 50 МГц (везде).
Автоматическая выгрузка: `run_all.py` (`_gpio_rows.json`). Строки «computed» разрешены вручную по сдвигам (см. колонку «Прим.»).

| Порт/пины | Режим | Функция инициализации (адрес вызова) | Назначение | Прим./доказательства |
|---|---|---|---|---|
| PE3 | OUT_PP | LCD_GPIO_FSMC_Init 0x080153E4 (0x08015446) | LCD CS (ручной) | `GPIO_ResetBits(GPIOE,8)` в начале `LCD_WriteBuffer` 0x08015920, `SetBits` 0x0801593C |
| PE5 | OUT_PP | то же (0x08015446) | LCD RESET | `LCD_Reset` 0x08015252: ResetBits/SetBits(GPIOE,0x20) |
| PC9 | OUT_PP | 0x0801546A | LCD подсветка | ResetBits при инициализации; SetBits(GPIOC) в конце `LCD_Init` 0x080156C4 |
| PD0,1,4,5,8,9,10,14,15 | AF_PP | 0x0801548C | FSMC: D2,D3,NOE,NWE,D13,D14,D15,D0,D1 | маска 0xC733 |
| PE4,7–15 | AF_PP | 0x0801549C | FSMC: PE4=A20 (RS), PE7–PE15=D4…D12 | маска 0xFF90 |
| PB13 | AF_PP | SD_SPI2_Init 0x08014AC8 (0x08014AF6) | SPI2 SCK | `asrs r0,r5,#1` (r5=0x4000) |
| PB14 | AF_PP | 0x08014B02 | SPI2 MISO | |
| PB15 | AF_PP | 0x08014B10 | SPI2 MOSI | |
| PB12 | OUT_PP | 0x08014B28 | SD CS | `SetBits(GPIOB,PB12)` 0x08014B44 |
| PB11 | IPU | 0x08014B3C | SD card-detect | `ReadInputDataBit(GPIOB,0x800)` 0x08014D0C |
| PC4 | OUT_PP, затем IPU | Touch_GPIO_Init 0x08016A2C (0x08016A50, **0x08016AAA**) | XPT2046 CS (см. TOUCH) | итоговый режим — IPU! |
| PA5, PA7 | OUT_PP | 0x08016A68 | XPT2046 SCK, MOSI (программный SPI) | |
| PA6 | IPU | 0x08016A7C | XPT2046 MISO | чтение `GPIO_ReadInputDataBit(GPIOA,0x40)` 0x0801653C |
| PC5 | IPU | 0x08016A8E | XPT2046 PENIRQ (опрос) | `ReadInputDataBit(GPIOC,0x20)` 0x08016BBC |
| PE2 | OUT_PP | 0x080171F4 (0x0801721C) | неизвестно (выход, переключается `0x08017222`/`0x0801723A`) | **UNRESOLVED**: возможно реле/питание/светодиод |
| PA8 | OUT_PP | USART1_Init 0x0801738A (0x080173B8) | сброс принтера | + `SetBits(GPIOA,PA8)` 0x080173C0 (в покое = 1) |
| PA9 | AF_PP | 0x080173D8 | USART1 TX | |
| PA10 | IPU | 0x080173EC | USART1 RX | |
| PA2 | AF_PP | Buzzer 0x08017520 (0x0801754C) | TIM5_CH3 PWM зуммер | |
| PA4 | AIN | DAC_Init 0x080175C0 (0x080175EC) | DAC_OUT1 | назначение выхода неизвестно (UNRESOLVED) |
| PD0,1,4,5,7,11,12,14,15 | AF_PP | NAND_GPIO_FSMC_Init 0x0801762C (0x0801765C) | NAND: D2,D3,NOE,NWE,**NCE2=PD7**,CLE=PD11,ALE=PD12,D0,D1 | |
| PE7–10 | AF_PP | 0x0801766E | NAND D4–D7 | |
| PD6 | IPU | 0x08017686 | NAND NWAIT/RB | |
| PE0 | IPU | 0x08017694 | неизвестно (рядом с NAND; возможно NBL0/пробный вход) | UNRESOLVED |
| PB3, PB5, PC7, PA15 | AF_PP | SPI3_DMA_Init 0x08017DCE | SPI3 (ремап) — **нет статических вызовов** | мёртвый/неиспользуемый код |

**Образ A (загрузчик):** функция `GPIO_Init` из B в образе A отсутствует (поиск по байтовой сигнатуре); конфигурация GPIO образа A не восстановлена — см. UNRESOLVED.md.
**Порты, не найденные в B:** GPIOF/G; PB0–PB10 (кроме SPI3-мёртвого кода) не настраиваются.
