# FUNCTION_INDEX

Всего функций: см. `disassembly/functions.json` (1126 записей: образ A = 533, образ B = 593). Колонки: адрес, конец (включая literal pool), размер, образ, имя, уверенность (high/medium/low — ручная; auto — только автоматическое описание), число вызываемых/вызывающих, затронутая периферия, описание. Полные списки callers/callees/evidence — в JSON.

Имена `sub_XXXXXXXX` — автоматические; описание `auto:` — только факты (периферия, строки, отсутствие вызовов), не интерпретация.

| Address | End | Size | Img | Name | Conf. | Calls (n) | Called by (n) | Peripherals | Description |
|---|---|---|---|---|---|---|---|---|---|
| 0x08000130 | 0x08000144 | 20 | A | A_startup_stub | high | 1 | 0 | - | SP=0x20007FC8, scatterload, bx 0x08000175 |
| 0x08000138 | 0x08000140 | 8 | A | sub_08000138 | auto | 0 | 1 | - | unknown |
| 0x08000144 | 0x08000174 | 48 | A | sub_08000144 | auto | 0 | 1 | - | unknown |
| 0x08000174 | 0x08000210 | 156 | A | A_main_bootloader | high | 8 | 0 | - | init, optional SD update path, validate 0x08010000 MSP (&0x2FFE0000==0x20000000), MSR MSP, jump to *(0x0801000 |
| 0x080001E8 | 0x080001F6 | 14 | A | sub_080001E8 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08000220 | 0x0800022A | 10 | A | sub_08000220 | auto | 0 | 0 | SCB | auto: touches SCB / no static callers (dead code or called via pointer) |
| 0x0800022A | 0x0800028E | 100 | A | sub_0800022A | auto | 0 | 2 | SCB | auto: touches SCB |
| 0x0800028E | 0x0800029C | 14 | A | sub_0800028E | auto | 0 | 1 | SCB | auto: touches SCB |
| 0x0800029C | 0x080002F0 | 84 | A | sub_0800029C | auto | 0 | 0 | SCB | auto: touches SCB / no static callers (dead code or called via pointer) |
| 0x080002BE | 0x080002E6 | 40 | A | sub_080002BE | auto | 0 | 0 | SysTick | auto: touches SysTick / no static callers (dead code or called via pointer) |
| 0x080002FC | 0x08000440 | 324 | A | sub_080002FC | auto | 0 | 0 | DMA1,DMA2 | auto: touches DMA1, DMA2 / no static callers (dead code or called via pointer) |
| 0x08000440 | 0x0800047C | 60 | A | sub_08000440 | auto | 0 | 1 | - | unknown |
| 0x0800047C | 0x08000496 | 26 | A | sub_0800047C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08000496 | 0x080004AE | 24 | A | sub_08000496 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080004AE | 0x080004C0 | 18 | A | sub_080004AE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080004C4 | 0x080004CC | 8 | A | sub_080004C4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080004CC | 0x080004F4 | 40 | A | sub_080004CC | auto | 0 | 0 | DMA2,DMA1 | auto: touches DMA2, DMA1 / no static callers (dead code or called via pointer) |
| 0x080004F4 | 0x0800054C | 88 | A | sub_080004F4 | auto | 0 | 0 | DMA2,DMA1 | auto: touches DMA2, DMA1 / no static callers (dead code or called via pointer) |
| 0x0800050A | 0x08000550 | 70 | A | sub_0800050A | auto | 0 | 0 | DMA2,DMA1 | auto: touches DMA2, DMA1 / no static callers (dead code or called via pointer) |
| 0x08000532 | 0x08000550 | 30 | A | sub_08000532 | auto | 0 | 0 | DMA2,DMA1 | auto: touches DMA2, DMA1 / no static callers (dead code or called via pointer) |
| 0x08000550 | 0x0800056C | 28 | A | sub_08000550 | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x0800056C | 0x080005FA | 142 | A | sub_0800056C | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x080005FA | 0x0800060A | 16 | A | sub_080005FA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800060A | 0x0800061A | 16 | A | sub_0800060A | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x0800061A | 0x08000668 | 78 | A | sub_0800061A | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x08000630 | 0x08000668 | 56 | A | sub_08000630 | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x08000638 | 0x08000668 | 48 | A | sub_08000638 | auto | 0 | 1 | EXTI | auto: touches EXTI |
| 0x0800065A | 0x08000668 | 14 | A | sub_0800065A | auto | 0 | 1 | EXTI | auto: touches EXTI |
| 0x0800066C | 0x0800067E | 18 | A | sub_0800066C | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x0800067E | 0x08000694 | 22 | A | sub_0800067E | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000694 | 0x080006AA | 22 | A | sub_08000694 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080006AA | 0x080006B6 | 12 | A | FLASH_Unlock | high | 0 | 2 | FLASH_IF | KEYR=0x45670123, 0xCDEF89AB |
| 0x080006B6 | 0x080006C2 | 12 | A | FLASH_Unlock_dup | high | 0 | 0 | FLASH_IF | duplicate of FLASH_Unlock |
| 0x080006C2 | 0x080006D0 | 14 | A | sub_080006C2 | auto | 0 | 2 | FLASH_IF | auto: touches FLASH_IF |
| 0x080006D0 | 0x080006DE | 14 | A | sub_080006D0 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080006DE | 0x0800070E | 48 | A | sub_080006DE | auto | 0 | 2 | FLASH_IF | auto: touches FLASH_IF |
| 0x0800070E | 0x08000734 | 38 | A | sub_0800070E | auto | 1 | 9 | - | unknown |
| 0x08000734 | 0x0800077C | 72 | A | sub_08000734 | auto | 1 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x0800077C | 0x080007C0 | 68 | A | sub_0800077C | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080007C0 | 0x080007E6 | 38 | A | sub_080007C0 | auto | 1 | 1 | - | unknown |
| 0x080007E6 | 0x0800082A | 68 | A | sub_080007E6 | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x0800082A | 0x0800083E | 20 | A | sub_0800082A | auto | 0 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x0800083E | 0x080008D4 | 150 | A | sub_0800083E | auto | 2 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x080008D4 | 0x0800093A | 102 | A | sub_080008D4 | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x0800093A | 0x08000976 | 60 | A | sub_0800093A | auto | 1 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x08000976 | 0x080009BE | 72 | A | sub_08000976 | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080009BE | 0x08000A86 | 200 | A | sub_080009BE | auto | 1 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x08000A86 | 0x08000B22 | 156 | A | sub_08000A86 | auto | 1 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x08000B22 | 0x08000B7A | 88 | A | sub_08000B22 | auto | 1 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x08000B7A | 0x08000B82 | 8 | A | sub_08000B7A | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000B82 | 0x08000B88 | 6 | A | sub_08000B82 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000B88 | 0x08000B9C | 20 | A | sub_08000B88 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000B9C | 0x08000BB6 | 26 | A | sub_08000B9C | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000BB6 | 0x08000C1C | 102 | A | sub_08000BB6 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000BE0 | 0x08000C1C | 60 | A | sub_08000BE0 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000BE6 | 0x08000C1C | 54 | A | sub_08000BE6 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08000C28 | 0x08000C5E | 54 | A | sub_08000C28 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08000C5E | 0x08000C9C | 62 | A | sub_08000C5E | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08000C9C | 0x08000CC0 | 36 | A | sub_08000C9C | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08000CC0 | 0x08000DA6 | 230 | A | sub_08000CC0 | auto | 0 | 1 | - | unknown |
| 0x08000DA6 | 0x08000E2A | 132 | A | sub_08000DA6 | auto | 0 | 1 | FSMC_REGS | auto: touches FSMC_REGS |
| 0x08000E2A | 0x08000EAC | 130 | A | sub_08000E2A | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08000EAC | 0x08000F1E | 114 | A | sub_08000EAC | auto | 0 | 1 | - | unknown |
| 0x08000F1E | 0x08000F54 | 54 | A | sub_08000F1E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08000F54 | 0x08000F90 | 60 | A | sub_08000F54 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08000F90 | 0x08000FBE | 46 | A | sub_08000F90 | auto | 0 | 1 | - | unknown |
| 0x08000FBE | 0x08001014 | 86 | A | sub_08000FBE | auto | 0 | 1 | FSMC_REGS | auto: touches FSMC_REGS |
| 0x08001014 | 0x08001060 | 76 | A | sub_08001014 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08001040 | 0x0800109A | 90 | A | sub_08001040 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x0800109A | 0x080010B2 | 24 | A | sub_0800109A | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x080010B2 | 0x08001132 | 128 | A | sub_080010B2 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08001132 | 0x08001168 | 54 | A | sub_08001132 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08001168 | 0x080011A6 | 62 | A | sub_08001168 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x080011A6 | 0x080011E6 | 64 | A | sub_080011A6 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x080011E6 | 0x08001230 | 74 | A | sub_080011E6 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08001234 | 0x080012E0 | 172 | A | sub_08001234 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080012E0 | 0x080012F4 | 20 | A | sub_080012E0 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080012F4 | 0x0800140A | 278 | A | sub_080012F4 | auto | 0 | 9 | - | unknown |
| 0x0800140A | 0x0800141A | 16 | A | sub_0800140A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800141A | 0x0800142C | 18 | A | sub_0800141A | auto | 0 | 12 | - | unknown |
| 0x0800142C | 0x08001434 | 8 | A | sub_0800142C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001434 | 0x08001446 | 18 | A | sub_08001434 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001446 | 0x0800144E | 8 | A | sub_08001446 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800144E | 0x08001452 | 4 | A | sub_0800144E | auto | 0 | 21 | - | unknown |
| 0x08001452 | 0x08001456 | 4 | A | sub_08001452 | auto | 0 | 20 | - | unknown |
| 0x08001456 | 0x08001460 | 10 | A | sub_08001456 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001464 | 0x08001476 | 18 | A | sub_08001464 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001476 | 0x08001490 | 26 | A | sub_08001476 | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x08001490 | 0x08001496 | 6 | A | sub_08001490 | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x08001496 | 0x08001520 | 138 | A | sub_08001496 | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x08001520 | 0x0800158C | 108 | A | sub_08001520 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001562 | 0x08001590 | 46 | A | sub_08001562 | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x08001590 | 0x080015D0 | 64 | A | sub_08001590 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080015D0 | 0x08001616 | 70 | A | sub_080015D0 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001616 | 0x0800164E | 56 | A | sub_08001616 | auto | 0 | 1 | RCC | auto: touches RCC |
| 0x0800164E | 0x08001686 | 56 | A | sub_0800164E | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001686 | 0x0800169A | 20 | A | sub_08001686 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0800169A | 0x080016A0 | 6 | A | sub_0800169A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016A0 | 0x080016B8 | 24 | A | sub_080016A0 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016B8 | 0x080016BE | 6 | A | sub_080016B8 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016BE | 0x080016D0 | 18 | A | sub_080016BE | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016D0 | 0x080016DA | 10 | A | sub_080016D0 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016DA | 0x080016EC | 18 | A | sub_080016DA | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016EC | 0x080016FE | 18 | A | sub_080016EC | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080016FE | 0x08001712 | 20 | A | sub_080016FE | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001712 | 0x0800172C | 26 | A | sub_08001712 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0800172C | 0x08001734 | 8 | A | sub_0800172C | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001734 | 0x08001746 | 18 | A | sub_08001734 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001746 | 0x08001778 | 50 | A | sub_08001746 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001778 | 0x0800177E | 6 | A | sub_08001778 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0800177E | 0x0800178A | 12 | A | sub_0800177E | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0800178A | 0x08001792 | 8 | A | sub_0800178A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001792 | 0x08001852 | 192 | A | sub_08001792 | auto | 0 | 2 | RCC | auto: touches RCC |
| 0x08001852 | 0x0800186C | 26 | A | sub_08001852 | auto | 0 | 3 | RCC | auto: touches RCC |
| 0x0800186C | 0x08001886 | 26 | A | sub_0800186C | auto | 0 | 9 | RCC | auto: touches RCC |
| 0x08001886 | 0x080018A0 | 26 | A | sub_08001886 | auto | 0 | 3 | RCC | auto: touches RCC |
| 0x080018A0 | 0x080018BA | 26 | A | sub_080018A0 | auto | 0 | 5 | RCC | auto: touches RCC |
| 0x080018BA | 0x08001914 | 90 | A | sub_080018BA | auto | 0 | 3 | RCC | auto: touches RCC |
| 0x080018D4 | 0x080018DC | 8 | A | sub_080018D4 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080018DC | 0x08001920 | 68 | A | sub_080018DC | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080018E2 | 0x08001914 | 50 | A | sub_080018E2 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080018E8 | 0x08001914 | 44 | A | sub_080018E8 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080018F6 | 0x08001914 | 30 | A | sub_080018F6 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0800190A | 0x08001914 | 10 | A | sub_0800190A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08001934 | 0x08001980 | 76 | A | sub_08001934 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001980 | 0x080019BC | 60 | A | sub_08001980 | auto | 0 | 2 | - | unknown |
| 0x080019BC | 0x08001A9E | 226 | A | sub_080019BC | auto | 1 | 1 | - | unknown |
| 0x08001A9E | 0x08001AB6 | 24 | A | sub_08001A9E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001AB6 | 0x08001ACA | 20 | A | sub_08001AB6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001ACA | 0x08001AE2 | 24 | A | sub_08001ACA | auto | 0 | 2 | - | unknown |
| 0x08001AE2 | 0x08001AFA | 24 | A | sub_08001AE2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001AFA | 0x08001B1A | 32 | A | sub_08001AFA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B1A | 0x08001B2C | 18 | A | sub_08001B1A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B2C | 0x08001B30 | 4 | A | sub_08001B2C | auto | 0 | 1 | - | unknown |
| 0x08001B30 | 0x08001B36 | 6 | A | sub_08001B30 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B36 | 0x08001B54 | 30 | A | sub_08001B36 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B54 | 0x08001B6C | 24 | A | sub_08001B54 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B6C | 0x08001B7E | 18 | A | sub_08001B6C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B7E | 0x08001B88 | 10 | A | sub_08001B7E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001B88 | 0x08001BA0 | 24 | A | sub_08001B88 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001BA0 | 0x08001BB0 | 16 | A | sub_08001BA0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001BB0 | 0x08001BB6 | 6 | A | sub_08001BB0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001BB6 | 0x08001BD2 | 28 | A | sub_08001BB6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001BD2 | 0x08001BE4 | 18 | A | sub_08001BD2 | auto | 0 | 1 | - | unknown |
| 0x08001BE4 | 0x08001BEA | 6 | A | sub_08001BE4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001BEA | 0x08001C1E | 52 | A | sub_08001BEA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001C1E | 0x08001C32 | 20 | A | sub_08001C1E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001C40 | 0x08001DE8 | 424 | A | sub_08001C40 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001DE8 | 0x08001E62 | 122 | A | sub_08001DE8 | auto | 0 | 1 | - | unknown |
| 0x08001E62 | 0x08001EE6 | 132 | A | sub_08001E62 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001EE6 | 0x08001F80 | 154 | A | sub_08001EE6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08001F80 | 0x0800205C | 220 | A | sub_08001F80 | auto | 0 | 1 | - | unknown |
| 0x08002016 | 0x080020CC | 182 | A | sub_08002016 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080020CC | 0x080020E6 | 26 | A | sub_080020CC | auto | 0 | 1 | - | unknown |
| 0x080020E6 | 0x08002168 | 130 | A | sub_080020E6 | auto | 0 | 1 | - | unknown |
| 0x08002168 | 0x0800217A | 18 | A | sub_08002168 | auto | 0 | 1 | - | unknown |
| 0x0800217A | 0x080021F4 | 122 | A | sub_0800217A | auto | 0 | 1 | - | unknown |
| 0x080021F4 | 0x0800220E | 26 | A | sub_080021F4 | auto | 0 | 2 | - | unknown |
| 0x0800220E | 0x08002290 | 130 | A | sub_0800220E | auto | 0 | 3 | - | unknown |
| 0x08002290 | 0x080022A2 | 18 | A | sub_08002290 | auto | 0 | 2 | - | unknown |
| 0x080022A2 | 0x0800230E | 108 | A | sub_080022A2 | auto | 0 | 3 | - | unknown |
| 0x0800230E | 0x080023A4 | 150 | A | sub_0800230E | auto | 8 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080023A4 | 0x08002420 | 124 | A | sub_080023A4 | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002420 | 0x08002440 | 32 | A | sub_08002420 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002440 | 0x08002452 | 18 | A | sub_08002440 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002452 | 0x08002466 | 20 | A | sub_08002452 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002466 | 0x08002478 | 18 | A | sub_08002466 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002478 | 0x0800248A | 18 | A | sub_08002478 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080024A0 | 0x080024B8 | 24 | A | sub_080024A0 | auto | 0 | 1 | - | unknown |
| 0x080024B8 | 0x080024D6 | 30 | A | sub_080024B8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080024D6 | 0x080024E8 | 18 | A | sub_080024D6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080024EC | 0x080024F6 | 10 | A | sub_080024EC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080024F6 | 0x08002508 | 18 | A | sub_080024F6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002508 | 0x08002514 | 12 | A | sub_08002508 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002514 | 0x08002526 | 18 | A | sub_08002514 | auto | 0 | 2 | - | unknown |
| 0x08002526 | 0x0800253E | 24 | A | sub_08002526 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800253E | 0x0800257C | 62 | A | sub_0800253E | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800257C | 0x08002598 | 28 | A | sub_0800257C | auto | 0 | 2 | - | unknown |
| 0x08002598 | 0x080025CE | 54 | A | sub_08002598 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080025CE | 0x080025EE | 32 | A | sub_080025CE | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080025EE | 0x080025F4 | 6 | A | sub_080025EE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080025F4 | 0x08002606 | 18 | A | sub_080025F4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002606 | 0x08002648 | 66 | A | sub_08002606 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002648 | 0x0800265A | 18 | A | sub_08002648 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800265A | 0x08002674 | 26 | A | sub_0800265A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002674 | 0x08002686 | 18 | A | sub_08002674 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002686 | 0x080026A0 | 26 | A | sub_08002686 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080026A0 | 0x080026B8 | 24 | A | sub_080026A0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080026B8 | 0x080026D0 | 24 | A | sub_080026B8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080026D0 | 0x080026E8 | 24 | A | sub_080026D0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080026E8 | 0x08002700 | 24 | A | sub_080026E8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002700 | 0x08002712 | 18 | A | sub_08002700 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002712 | 0x0800272C | 26 | A | sub_08002712 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800272C | 0x0800273E | 18 | A | sub_0800272C | auto | 0 | 1 | - | unknown |
| 0x0800273E | 0x08002758 | 26 | A | sub_0800273E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002758 | 0x0800276A | 18 | A | sub_08002758 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800276A | 0x08002784 | 26 | A | sub_0800276A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002784 | 0x08002796 | 18 | A | sub_08002784 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002796 | 0x080027B0 | 26 | A | sub_08002796 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080027B0 | 0x080027C2 | 18 | A | sub_080027B0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080027C2 | 0x080027DA | 24 | A | sub_080027C2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080027DA | 0x080027EC | 18 | A | sub_080027DA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080027EC | 0x08002804 | 24 | A | sub_080027EC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002804 | 0x08002816 | 18 | A | sub_08002804 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002816 | 0x08002828 | 18 | A | sub_08002816 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002828 | 0x08002842 | 26 | A | sub_08002828 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002842 | 0x0800285C | 26 | A | sub_08002842 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800285C | 0x08002876 | 26 | A | sub_0800285C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002876 | 0x08002890 | 26 | A | sub_08002876 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002890 | 0x080028AA | 26 | A | sub_08002890 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080028AA | 0x080028C8 | 30 | A | sub_080028AA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080028C8 | 0x080028E6 | 30 | A | sub_080028C8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080028E6 | 0x08002938 | 82 | A | sub_080028E6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002938 | 0x08002950 | 24 | A | sub_08002938 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002950 | 0x08002968 | 24 | A | sub_08002950 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002968 | 0x08002980 | 24 | A | sub_08002968 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002980 | 0x08002992 | 18 | A | sub_08002980 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002992 | 0x080029A4 | 18 | A | sub_08002992 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080029A4 | 0x080029B6 | 18 | A | sub_080029A4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080029B6 | 0x080029C8 | 18 | A | sub_080029B6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080029E2 | 0x080029F4 | 18 | A | sub_080029E2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080029F4 | 0x080029FA | 6 | A | sub_080029F4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080029FA | 0x08002A00 | 6 | A | sub_080029FA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A00 | 0x08002A06 | 6 | A | sub_08002A00 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A06 | 0x08002A0E | 8 | A | sub_08002A06 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A0E | 0x08002A14 | 6 | A | sub_08002A0E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A14 | 0x08002A1A | 6 | A | sub_08002A14 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A1A | 0x08002A2C | 18 | A | sub_08002A1A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A2C | 0x08002A32 | 6 | A | sub_08002A2C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A32 | 0x08002A54 | 34 | A | sub_08002A32 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A54 | 0x08002A5A | 6 | A | sub_08002A54 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002A5C | 0x08002AE2 | 134 | A | sub_08002A5C | auto | 2 | 1 | - | unknown |
| 0x08002AE2 | 0x08002BB4 | 210 | A | sub_08002AE2 | auto | 1 | 1 | - | unknown |
| 0x08002BB4 | 0x08002BCC | 24 | A | sub_08002BB4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002BCC | 0x08002BEE | 34 | A | sub_08002BCC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002BEE | 0x08002BFA | 12 | A | sub_08002BEE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002BFA | 0x08002C12 | 24 | A | sub_08002BFA | auto | 0 | 1 | - | unknown |
| 0x08002C12 | 0x08002C5C | 74 | A | sub_08002C12 | auto | 0 | 1 | - | unknown |
| 0x08002C5C | 0x08002C6E | 18 | A | sub_08002C5C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002C6E | 0x08002C80 | 18 | A | sub_08002C6E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002C80 | 0x08002C92 | 18 | A | sub_08002C80 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002C92 | 0x08002CAA | 24 | A | sub_08002C92 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002CAA | 0x08002CBC | 18 | A | sub_08002CAA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002CBC | 0x08002CD4 | 24 | A | sub_08002CBC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002CD4 | 0x08002CDC | 8 | A | sub_08002CD4 | auto | 0 | 1 | - | unknown |
| 0x08002CDC | 0x08002CE6 | 10 | A | sub_08002CDC | auto | 0 | 1 | - | unknown |
| 0x08002CE6 | 0x08002CF0 | 10 | A | sub_08002CE6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002CF0 | 0x08002D00 | 16 | A | sub_08002CF0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D00 | 0x08002D10 | 16 | A | sub_08002D00 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D10 | 0x08002D28 | 24 | A | sub_08002D10 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D28 | 0x08002D40 | 24 | A | sub_08002D28 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D40 | 0x08002D58 | 24 | A | sub_08002D40 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D58 | 0x08002D6E | 22 | A | sub_08002D58 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D6E | 0x08002D86 | 24 | A | sub_08002D6E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D86 | 0x08002D98 | 18 | A | sub_08002D86 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002D98 | 0x08002DB0 | 24 | A | sub_08002D98 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002DB0 | 0x08002DCA | 26 | A | sub_08002DB0 | auto | 0 | 1 | - | unknown |
| 0x08002DCA | 0x08002DDC | 18 | A | sub_08002DCA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002DDC | 0x08002E30 | 84 | A | sub_08002DDC | auto | 0 | 1 | - | unknown |
| 0x08002E30 | 0x08002E4E | 30 | A | sub_08002E30 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08002E64 | 0x08002E66 | 2 | A | sub_08002E64 | auto | 0 | 0 | - | unknown |
| 0x08002E66 | 0x08002E6A | 4 | A | sub_08002E66 | auto | 0 | 0 | - | unknown |
| 0x08002E6A | 0x08002E6E | 4 | A | sub_08002E6A | auto | 0 | 0 | - | unknown |
| 0x08002E6E | 0x08002E72 | 4 | A | sub_08002E6E | auto | 0 | 0 | - | unknown |
| 0x08002E72 | 0x08002E76 | 4 | A | sub_08002E72 | auto | 0 | 0 | - | unknown |
| 0x08002E76 | 0x08002E78 | 2 | A | sub_08002E76 | auto | 0 | 0 | - | unknown |
| 0x08002E78 | 0x08002E7A | 2 | A | sub_08002E78 | auto | 0 | 0 | - | unknown |
| 0x08002E7A | 0x08002E7C | 2 | A | sub_08002E7A | auto | 0 | 0 | - | unknown |
| 0x08002E7C | 0x08002E7E | 2 | A | sub_08002E7C | auto | 0 | 0 | - | unknown |
| 0x08002E80 | 0x08002EA0 | 32 | A | sub_08002E80 | auto | 1 | 2 | - | unknown |
| 0x08002EA0 | 0x08002EAC | 12 | A | sub_08002EA0 | auto | 0 | 2 | - | unknown |
| 0x08002EAC | 0x08002EF0 | 68 | A | sub_08002EAC | auto | 2 | 6 | - | unknown |
| 0x08002EF0 | 0x08002F2C | 60 | A | sub_08002EF0 | auto | 2 | 6 | - | unknown |
| 0x08002F2C | 0x08002F94 | 104 | A | sub_08002F2C | auto | 4 | 1 | - | unknown |
| 0x08002F8A | 0x08002F8E | 4 | A | sub_08002F8A | auto | 0 | 3 | - | unknown |
| 0x08002F94 | 0x08002FAE | 26 | A | sub_08002F94 | auto | 0 | 7 | - | unknown |
| 0x08002FAE | 0x08002FC2 | 20 | A | sub_08002FAE | auto | 0 | 5 | - | unknown |
| 0x08002FC2 | 0x08002FE8 | 38 | A | sub_08002FC2 | auto | 0 | 2 | - | unknown |
| 0x08002FE8 | 0x08002FFC | 20 | A | sub_08002FE8 | auto | 0 | 1 | - | unknown |
| 0x08002FFC | 0x0800306E | 114 | A | sub_08002FFC | auto | 2 | 13 | - | unknown |
| 0x0800306E | 0x08003138 | 202 | A | sub_0800306E | auto | 4 | 6 | - | unknown |
| 0x08003138 | 0x08003260 | 296 | A | sub_08003138 | auto | 1 | 8 | - | unknown |
| 0x08003260 | 0x080033D0 | 368 | A | sub_08003260 | auto | 1 | 3 | - | unknown |
| 0x080033D0 | 0x08003438 | 104 | A | sub_080033D0 | auto | 2 | 4 | - | unknown |
| 0x08003438 | 0x080034EE | 182 | A | sub_08003438 | auto | 2 | 4 | - | unknown |
| 0x080034EE | 0x08003508 | 26 | A | sub_080034EE | auto | 0 | 7 | - | unknown |
| 0x08003508 | 0x080035AE | 166 | A | sub_08003508 | auto | 2 | 7 | - | unknown |
| 0x080035AE | 0x080036DC | 302 | A | sub_080035AE | auto | 5 | 5 | - | unknown |
| 0x080036DC | 0x0800374C | 112 | A | sub_080036DC | auto | 0 | 1 | - | unknown |
| 0x0800374C | 0x080037A6 | 90 | A | sub_0800374C | auto | 0 | 1 | - | unknown |
| 0x080037A6 | 0x08003820 | 122 | A | sub_080037A6 | auto | 0 | 1 | - | unknown |
| 0x08003820 | 0x080038B0 | 144 | A | sub_08003820 | auto | 1 | 1 | - | unknown |
| 0x080038B0 | 0x080038D0 | 32 | A | sub_080038B0 | auto | 0 | 3 | - | unknown |
| 0x080038D0 | 0x080039BC | 236 | A | sub_080038D0 | auto | 6 | 2 | - | unknown |
| 0x080039BC | 0x08003A7A | 190 | A | sub_080039BC | auto | 4 | 2 | - | unknown |
| 0x08003A7A | 0x08003C08 | 398 | A | sub_08003A7A | auto | 9 | 3 | - | unknown |
| 0x08003C08 | 0x08003C68 | 96 | A | sub_08003C08 | auto | 3 | 2 | - | unknown |
| 0x08003C68 | 0x08003E72 | 522 | A | sub_08003C68 | auto | 3 | 1 | - | auto: strings: '+,;[=]' |
| 0x08003E72 | 0x08003F96 | 292 | A | sub_08003E72 | auto | 1 | 2 | - | unknown |
| 0x08003F96 | 0x0800403A | 164 | A | sub_08003F96 | auto | 3 | 8 | - | unknown |
| 0x0800403A | 0x080040B8 | 126 | A | sub_0800403A | auto | 2 | 1 | - | auto: strings: 'FAT'; 'FAT32' |
| 0x080040B8 | 0x080043A2 | 746 | A | sub_080040B8 | auto | 4 | 9 | - | unknown |
| 0x080043A2 | 0x080043CC | 42 | A | sub_080043A2 | auto | 1 | 6 | - | unknown |
| 0x080043CC | 0x080043F2 | 38 | A | sub_080043CC | auto | 0 | 1 | - | unknown |
| 0x080043F2 | 0x080045A6 | 436 | A | sub_080043F2 | auto | 6 | 5 | - | unknown |
| 0x080045A6 | 0x08004758 | 434 | A | sub_080045A6 | auto | 6 | 10 | - | unknown |
| 0x08004758 | 0x0800493C | 484 | A | sub_08004758 | auto | 6 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800493C | 0x080049F4 | 184 | A | sub_0800493C | auto | 5 | 1 | - | unknown |
| 0x080049F4 | 0x08004A0A | 22 | A | sub_080049F4 | auto | 1 | 1 | - | unknown |
| 0x08004A0A | 0x08004BD0 | 454 | A | sub_08004A0A | auto | 6 | 5 | - | unknown |
| 0x08004BD0 | 0x08004C58 | 136 | A | sub_08004BD0 | auto | 3 | 1 | - | unknown |
| 0x08004C58 | 0x08004CBC | 100 | A | sub_08004C58 | auto | 5 | 1 | - | unknown |
| 0x08004CBC | 0x08004CFE | 66 | A | sub_08004CBC | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08004CFE | 0x08004D9C | 158 | A | sub_08004CFE | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08004D9C | 0x08004E9C | 256 | A | sub_08004D9C | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08004E9C | 0x08004F5C | 192 | A | sub_08004E9C | auto | 8 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08004F5C | 0x080050EA | 398 | A | sub_08004F5C | auto | 11 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080050EA | 0x0800514C | 98 | A | sub_080050EA | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800514C | 0x080051A8 | 92 | A | sub_0800514C | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080051A8 | 0x080052CC | 292 | A | sub_080051A8 | auto | 8 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080052CC | 0x0800543C | 368 | A | sub_080052CC | auto | 7 | 2 | - | unknown |
| 0x0800543C | 0x0800549C | 96 | A | sub_0800543C | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800549C | 0x080054BC | 32 | A | sub_0800549C | auto | 1 | 1 | - | unknown |
| 0x080054BC | 0x08005526 | 106 | A | sub_080054BC | auto | 3 | 2 | - | unknown |
| 0x08005526 | 0x0800558E | 104 | A | sub_08005526 | auto | 3 | 2 | - | unknown |
| 0x0800558E | 0x080055F6 | 104 | A | sub_0800558E | auto | 3 | 1 | - | unknown |
| 0x080055F6 | 0x0800560C | 22 | A | sub_080055F6 | auto | 1 | 6 | - | unknown |
| 0x0800560C | 0x0800561A | 14 | A | sub_0800560C | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800561C | 0x0800564E | 50 | A | sub_0800561C | auto | 2 | 1 | - | unknown |
| 0x0800564E | 0x08005662 | 20 | A | sub_0800564E | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005662 | 0x08005732 | 208 | A | sub_08005662 | auto | 8 | 1 | - | unknown |
| 0x08005732 | 0x08005796 | 100 | A | sub_08005732 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005796 | 0x0800580A | 116 | A | sub_08005796 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800580A | 0x080058AA | 160 | A | sub_0800580A | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080058AA | 0x080058CE | 36 | A | sub_080058AA | auto | 1 | 1 | - | unknown |
| 0x080058CE | 0x08005916 | 72 | A | sub_080058CE | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005916 | 0x08005972 | 92 | A | sub_08005916 | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005972 | 0x08005A26 | 180 | A | sub_08005972 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005A26 | 0x08005A86 | 96 | A | sub_08005A26 | auto | 5 | 1 | - | unknown |
| 0x08005A86 | 0x08005AA0 | 26 | A | sub_08005A86 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005AA0 | 0x08005ABA | 26 | A | sub_08005AA0 | auto | 0 | 1 | - | unknown |
| 0x08005ABA | 0x08005B88 | 206 | A | sub_08005ABA | auto | 7 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005B88 | 0x08005C00 | 120 | A | sub_08005B88 | auto | 0 | 2 | - | unknown |
| 0x08005BCE | 0x08005C08 | 58 | A | sub_08005BCE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08005C08 | 0x08005C2A | 34 | A | sub_08005C08 | auto | 0 | 5 | - | unknown |
| 0x08005C2A | 0x08005C4C | 34 | A | sub_08005C2A | auto | 0 | 7 | - | unknown |
| 0x08005C4C | 0x08005D24 | 216 | A | sub_08005C4C | auto | 6 | 1 | - | unknown |
| 0x08005D24 | 0x08005D7E | 90 | A | sub_08005D24 | auto | 2 | 5 | - | unknown |
| 0x08005D7E | 0x08005DAE | 48 | A | sub_08005D7E | auto | 1 | 8 | SPI2 | auto: touches SPI2 |
| 0x08005DAE | 0x08005E30 | 130 | A | sub_08005DAE | auto | 5 | 6 | - | unknown |
| 0x08005E30 | 0x08005E9E | 110 | A | sub_08005E30 | auto | 4 | 1 | - | unknown |
| 0x08005E9E | 0x080060A0 | 514 | A | sub_08005E9E | auto | 8 | 2 | - | unknown |
| 0x080060A0 | 0x08006122 | 130 | A | sub_080060A0 | auto | 5 | 3 | - | unknown |
| 0x08006122 | 0x08006160 | 62 | A | sub_08006122 | auto | 3 | 1 | - | unknown |
| 0x08006160 | 0x080061D6 | 118 | A | sub_08006160 | auto | 6 | 1 | - | unknown |
| 0x080061D6 | 0x080062BA | 228 | A | sub_080061D6 | auto | 7 | 1 | - | unknown |
| 0x080062BA | 0x080062DC | 34 | A | sub_080062BA | auto | 1 | 2 | - | unknown |
| 0x080062DC | 0x08006300 | 36 | A | sub_080062DC | auto | 2 | 1 | - | unknown |
| 0x08006300 | 0x080063A6 | 166 | A | sub_08006300 | auto | 1 | 1 | - | unknown |
| 0x080063A6 | 0x080064A8 | 258 | A | sub_080063A6 | auto | 8 | 1 | - | unknown |
| 0x080064A8 | 0x080064B0 | 8 | A | sub_080064A8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080064B0 | 0x080064CE | 30 | A | sub_080064B0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080064CE | 0x080064EE | 32 | A | sub_080064CE | auto | 0 | 3 | - | unknown |
| 0x080064EE | 0x08006512 | 36 | A | sub_080064EE | auto | 3 | 1 | - | unknown |
| 0x08006512 | 0x0800651A | 8 | A | sub_08006512 | auto | 0 | 8 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x0800651A | 0x08006520 | 6 | A | sub_0800651A | auto | 0 | 1 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x08006520 | 0x08006526 | 6 | A | sub_08006520 | auto | 0 | 7 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x08006526 | 0x08006532 | 12 | A | sub_08006526 | auto | 1 | 9 | - | unknown |
| 0x08006532 | 0x08006592 | 96 | A | sub_08006532 | auto | 3 | 3 | - | unknown |
| 0x08006592 | 0x080065A8 | 22 | A | sub_08006592 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080065A8 | 0x080065B2 | 10 | A | sub_080065A8 | auto | 1 | 5 | - | unknown |
| 0x080065B2 | 0x080065FE | 76 | A | sub_080065B2 | auto | 2 | 5 | - | unknown |
| 0x080065FE | 0x08006686 | 136 | A | sub_080065FE | auto | 3 | 1 | - | unknown |
| 0x08006686 | 0x080066CE | 72 | A | sub_08006686 | auto | 3 | 5 | - | unknown |
| 0x080066CE | 0x080066FA | 44 | A | sub_080066CE | auto | 2 | 0 | - | auto: strings: '%d %d' / no static callers (dead code or called via pointer) |
| 0x080066FA | 0x080067F6 | 252 | A | sub_080066FA | auto | 7 | 1 | - | unknown |
| 0x080067F6 | 0x08006848 | 82 | A | sub_080067F6 | auto | 5 | 11 | - | unknown |
| 0x08006848 | 0x0800687C | 52 | A | sub_08006848 | auto | 2 | 1 | - | unknown |
| 0x0800687C | 0x08006A78 | 508 | A | sub_0800687C | auto | 8 | 1 | - | unknown |
| 0x08006A78 | 0x08006ACA | 82 | A | sub_08006A78 | auto | 2 | 3 | - | unknown |
| 0x08006ACA | 0x08006B34 | 106 | A | sub_08006ACA | auto | 4 | 1 | - | unknown |
| 0x08006B34 | 0x08006BA0 | 108 | A | sub_08006B34 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006BA0 | 0x08006BA6 | 6 | A | sub_08006BA0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006BA6 | 0x08006C18 | 114 | A | sub_08006BA6 | auto | 2 | 1 | - | unknown |
| 0x08006C18 | 0x08006C58 | 64 | A | sub_08006C18 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006C58 | 0x08006CC2 | 106 | A | sub_08006C58 | auto | 4 | 3 | - | unknown |
| 0x08006CC2 | 0x08006D1A | 88 | A | sub_08006CC2 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006D1A | 0x08006D86 | 108 | A | sub_08006D1A | auto | 1 | 1 | - | unknown |
| 0x08006D86 | 0x08006D9E | 24 | A | sub_08006D86 | auto | 1 | 1 | - | unknown |
| 0x08006D9E | 0x08006DEA | 76 | A | sub_08006D9E | auto | 1 | 1 | - | unknown |
| 0x08006DEA | 0x08006E58 | 110 | A | sub_08006DEA | auto | 5 | 1 | - | unknown |
| 0x08006E3C | 0x08006E78 | 60 | A | sub_08006E3C | auto | 3 | 3 | - | unknown |
| 0x08006E78 | 0x08006EB0 | 56 | A | sub_08006E78 | auto | 1 | 1 | - | unknown |
| 0x08006EB0 | 0x08006EEE | 62 | A | sub_08006EB0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006EEE | 0x08006F16 | 40 | A | sub_08006EEE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006F16 | 0x08006F30 | 26 | A | sub_08006F16 | auto | 1 | 1 | - | unknown |
| 0x08006F30 | 0x08006F38 | 8 | A | sub_08006F30 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08006F38 | 0x08006F9C | 100 | A | sub_08006F38 | auto | 1 | 2 | - | unknown |
| 0x08006F9C | 0x080070A6 | 266 | A | sub_08006F9C | auto | 4 | 0 | - | auto: strings: 'CANCE' / no static callers (dead code or called via pointer) |
| 0x080070A6 | 0x080070F2 | 76 | A | sub_080070A6 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080070F2 | 0x08007174 | 130 | A | sub_080070F2 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08007174 | 0x080071AA | 54 | A | sub_08007174 | auto | 2 | 1 | - | unknown |
| 0x080071AA | 0x080071C2 | 24 | A | sub_080071AA | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080071C4 | 0x08007384 | 448 | A | sub_080071C4 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08007384 | 0x080073B0 | 44 | A | sub_08007384 | auto | 1 | 1 | - | unknown |
| 0x080073B0 | 0x080073E0 | 48 | A | sub_080073B0 | auto | 1 | 1 | - | unknown |
| 0x080073E0 | 0x08007410 | 48 | A | sub_080073E0 | auto | 1 | 1 | - | unknown |
| 0x08007410 | 0x08007444 | 52 | A | sub_08007410 | auto | 2 | 1 | - | unknown |
| 0x08007444 | 0x0800753C | 248 | A | sub_08007444 | auto | 3 | 1 | - | unknown |
| 0x0800753C | 0x080075AC | 112 | A | sub_0800753C | auto | 1 | 1 | - | unknown |
| 0x080075AC | 0x0800783C | 656 | A | sub_080075AC | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800783C | 0x0800785C | 32 | A | sub_0800783C | auto | 0 | 1 | - | unknown |
| 0x0800785C | 0x0800787C | 32 | A | sub_0800785C | auto | 0 | 1 | - | unknown |
| 0x0800787C | 0x080078E2 | 102 | A | sub_0800787C | auto | 2 | 1 | - | unknown |
| 0x080078E2 | 0x08007908 | 38 | A | sub_080078E2 | auto | 2 | 1 | - | unknown |
| 0x08007908 | 0x0800797A | 114 | A | sub_08007908 | auto | 4 | 1 | - | unknown |
| 0x0800797A | 0x080079C0 | 70 | A | sub_0800797A | auto | 4 | 1 | - | unknown |
| 0x080079C0 | 0x08007A3C | 124 | A | sub_080079C0 | auto | 1 | 1 | - | unknown |
| 0x08007A3C | 0x08007A6A | 46 | A | sub_08007A3C | auto | 1 | 4 | - | unknown |
| 0x08007A6A | 0x08007B2A | 192 | A | sub_08007A6A | auto | 1 | 2 | - | unknown |
| 0x08007B2A | 0x08007B2C | 2 | A | sub_08007B2A | auto | 0 | 3 | - | unknown |
| 0x08007B2C | 0x08007B68 | 60 | A | sub_08007B2C | auto | 3 | 1 | - | unknown |
| 0x08007B68 | 0x08007B7C | 20 | A | sub_08007B68 | auto | 1 | 1 | - | unknown |
| 0x08007B7C | 0x08007FCE | 1106 | A | sub_08007B7C | auto | 17 | 0 | - | auto: strings: 'Touch Screen Adjust OK!' / no static callers (dead code or called via pointer) |
| 0x08007FCE | 0x08007FE2 | 20 | A | sub_08007FCE | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08007FE2 | 0x08007FFA | 24 | A | sub_08007FE2 | auto | 2 | 0 | - | unknown |
| 0x08007FFA | 0x08008070 | 118 | A | sub_08007FFA | auto | 6 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008070 | 0x0800807C | 12 | A | sub_08008070 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800807E | 0x08008092 | 20 | A | sub_0800807E | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008092 | 0x0800816C | 218 | A | sub_08008092 | auto | 6 | 2 | - | unknown |
| 0x0800816C | 0x08008266 | 250 | A | sub_0800816C | auto | 8 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008266 | 0x0800837E | 280 | A | sub_08008266 | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800837E | 0x08008416 | 152 | A | sub_0800837E | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008416 | 0x0800843A | 36 | A | sub_08008416 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800843A | 0x0800844A | 16 | A | sub_0800843A | auto | 0 | 2 | - | unknown |
| 0x0800844A | 0x08008484 | 58 | A | sub_0800844A | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008484 | 0x080084BE | 58 | A | sub_08008484 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080084BE | 0x080084EE | 48 | A | sub_080084BE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080084EE | 0x08008550 | 98 | A | sub_080084EE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008560 | 0x080085EC | 140 | A | sub_08008560 | auto | 0 | 0 | SysTick | auto: touches SysTick / no static callers (dead code or called via pointer) |
| 0x080085BA | 0x080085F0 | 54 | A | sub_080085BA | auto | 0 | 2 | - | unknown |
| 0x080085CE | 0x080085F0 | 34 | A | sub_080085CE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080085F0 | 0x0800861E | 46 | A | sub_080085F0 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800861E | 0x08008644 | 38 | A | sub_0800861E | auto | 0 | 1 | GPIOE | auto: touches GPIOE |
| 0x08008644 | 0x080086C8 | 132 | A | sub_08008644 | auto | 2 | 0 | GPIOE | auto: touches GPIOE / no static callers (dead code or called via pointer) |
| 0x080086C8 | 0x08008706 | 62 | A | sub_080086C8 | auto | 0 | 0 | RCC,TIM2,NVIC | auto: touches RCC, TIM2, NVIC / no static callers (dead code or called via pointer) |
| 0x08008706 | 0x0800875E | 88 | A | A_TIM2_IRQHandler | medium | 1 | 0 | TIM2 | tick ISR (bootloader) |
| 0x0800875E | 0x08008764 | 6 | A | sub_0800875E | auto | 0 | 6 | - | unknown |
| 0x08008764 | 0x080087A8 | 68 | A | sub_08008764 | auto | 0 | 5 | - | unknown |
| 0x0800876E | 0x08008786 | 24 | A | sub_0800876E | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008786 | 0x080087C0 | 58 | A | sub_08008786 | auto | 1 | 1 | - | unknown |
| 0x080087C0 | 0x080087C6 | 6 | A | sub_080087C0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080087C6 | 0x080087E6 | 32 | A | sub_080087C6 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080087E6 | 0x08008814 | 46 | A | sub_080087E6 | auto | 0 | 1 | - | unknown |
| 0x08008814 | 0x080088B6 | 162 | A | sub_08008814 | auto | 7 | 1 | - | unknown |
| 0x080088B6 | 0x080088D8 | 34 | A | A_uart_putc | medium | 0 | 1 | USART1 | USART1->DR write |
| 0x080088D8 | 0x080088EE | 22 | A | sub_080088D8 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080088EE | 0x08008916 | 40 | A | A_USART1_IRQHandler | medium | 3 | 0 | - | USART1 ISR (bootloader) |
| 0x08008916 | 0x080089BC | 166 | A | sub_08008916 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080089BC | 0x08008A5C | 160 | A | sub_080089BC | auto | 7 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008A3A | 0x08008A5C | 34 | A | sub_08008A3A | auto | 0 | 2 | TIM5 | auto: touches TIM5 |
| 0x08008A5C | 0x08008B0A | 174 | A | sub_08008A5C | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08008B0A | 0x08008B36 | 44 | A | A_NAND_ReadID | high | 0 | 1 | FSMC_BANK2(NAND) | CMD 0x90 ADDR 0 |
| 0x08008B36 | 0x08008B6E | 56 | A | sub_08008B36 | auto | 0 | 4 | - | unknown |
| 0x08008B6E | 0x08008B96 | 40 | A | A_NAND_ReadStatus | high | 0 | 1 | FSMC_BANK2(NAND) | CMD 0x70 |
| 0x08008B96 | 0x08008BC0 | 42 | A | sub_08008B96 | auto | 1 | 5 | - | unknown |
| 0x08008BC0 | 0x08008C8A | 202 | A | A_NAND_WritePage_Main | high | 3 | 4 | FSMC_BANK2(NAND) | CMD 0x80..0x10, column 0 |
| 0x08008C8A | 0x08008D48 | 190 | A | A_NAND_ReadPage_Main | high | 3 | 6 | FSMC_BANK2(NAND) | CMD 0x00..0x30, column 0 |
| 0x08008D48 | 0x08008E14 | 204 | A | A_NAND_WritePage_Spare | high | 3 | 0 | FSMC_BANK2(NAND) | CMD 0x80..0x10, column 0x0800 (spare) |
| 0x08008E14 | 0x08008EEA | 214 | A | A_NAND_ReadPage_Spare | high | 3 | 0 | FSMC_BANK2(NAND) | CMD 0x00..0x30, column 0x0800 (spare) |
| 0x08008EEA | 0x08008F58 | 110 | A | A_NAND_EraseBlock | high | 2 | 2 | FSMC_BANK2(NAND) | CMD 0x60..0xD0 |
| 0x08008F58 | 0x08008F62 | 10 | A | A_NAND_Reset | high | 0 | 0 | FSMC_BANK2(NAND) | CMD 0xFF |
| 0x08008F62 | 0x08008FB8 | 86 | A | sub_08008F62 | auto | 3 | 0 | - | auto: strings: 'Erase %d/%d' / no static callers (dead code or called via pointer) |
| 0x08008FB8 | 0x08008FD0 | 24 | A | sub_08008FB8 | auto | 0 | 1 | - | unknown |
| 0x08008FD0 | 0x08008FE6 | 22 | A | sub_08008FD0 | auto | 0 | 8 | - | unknown |
| 0x08008FE6 | 0x08009094 | 174 | A | sub_08008FE6 | auto | 2 | 1 | - | unknown |
| 0x08009094 | 0x08009174 | 224 | A | sub_08009094 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009174 | 0x080091A2 | 46 | A | sub_08009174 | auto | 0 | 1 | - | unknown |
| 0x080091A2 | 0x0800925A | 184 | A | sub_080091A2 | auto | 4 | 0 | RCC,AFIO,SPI3 | auto: touches RCC, AFIO, SPI3 / no static callers (dead code or called via pointer) |
| 0x0800925A | 0x080092BE | 100 | A | sub_0800925A | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080092BE | 0x080092F0 | 50 | A | sub_080092BE | auto | 0 | 1 | DMA2,SPI3 | auto: touches DMA2, SPI3 |
| 0x080092F0 | 0x0800930E | 30 | A | sub_080092F0 | auto | 0 | 4 | DMA2,SPI3 | auto: touches DMA2, SPI3 |
| 0x0800930E | 0x08009348 | 58 | A | sub_0800930E | auto | 2 | 2 | - | unknown |
| 0x08009348 | 0x080093F4 | 172 | A | sub_08009348 | auto | 2 | 0 | DMA2 | auto: touches DMA2 |
| 0x080093F4 | 0x08009428 | 52 | A | sub_080093F4 | auto | 0 | 1 | DMA2,SPI3 | auto: touches DMA2, SPI3 |
| 0x08009428 | 0x08009444 | 28 | A | sub_08009428 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009444 | 0x080094D6 | 146 | A | sub_08009444 | auto | 2 | 1 | DMA2 | auto: touches DMA2 |
| 0x080094D6 | 0x0800958C | 182 | A | sub_080094D6 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800954C | 0x08009564 | 24 | A | sub_0800954C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0800958C | 0x080095A4 | 24 | A | sub_0800958C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080095A4 | 0x080095AA | 6 | A | sub_080095A4 | auto | 0 | 1 | - | unknown |
| 0x080095AA | 0x080095D0 | 38 | A | sub_080095AA | auto | 1 | 1 | - | unknown |
| 0x080095D0 | 0x080095F2 | 34 | A | sub_080095D0 | auto | 1 | 1 | - | unknown |
| 0x080095F2 | 0x080096E8 | 246 | A | sub_080095F2 | auto | 5 | 2 | - | unknown |
| 0x080096D0 | 0x080096E0 | 16 | A | sub_080096D0 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080096E8 | 0x0800970C | 36 | A | A_Reset_Handler | high | 0 | 0 | - | Reset vector of bootloader |
| 0x08009702 | 0x08009704 | 2 | A | sub_08009702 | auto | 0 | 0 | - | unknown |
| 0x0800970C | 0x080097E2 | 214 | A | sub_0800970C | auto | 0 | 1 | RCC,FLASH_IF | auto: touches RCC, FLASH_IF |
| 0x080097E2 | 0x080097EA | 8 | A | sub_080097E2 | auto | 1 | 1 | - | unknown |
| 0x080097EA | 0x08009838 | 78 | A | sub_080097EA | auto | 1 | 1 | RCC,SCB | auto: touches RCC, SCB |
| 0x08009838 | 0x080098EC | 180 | A | sub_08009838 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080098EC | 0x080098FA | 14 | A | sub_080098EC | auto | 0 | 2 | - | unknown |
| 0x080098FA | 0x0800990C | 18 | A | sub_080098FA | auto | 0 | 1 | - | unknown |
| 0x0800990C | 0x08009C9E | 914 | A | sub_0800990C | auto | 0 | 1 | - | unknown |
| 0x080099B6 | 0x080099BC | 6 | A | sub_080099B6 | auto | 0 | 1 | - | unknown |
| 0x080099BC | 0x08009A20 | 100 | A | sub_080099BC | auto | 0 | 2 | - | unknown |
| 0x080099C0 | 0x08009A20 | 96 | A | sub_080099C0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009A20 | 0x08009C42 | 546 | A | sub_08009A20 | auto | 0 | 3 | - | unknown |
| 0x08009A9C | 0x08009C9E | 514 | A | sub_08009A9C | auto | 0 | 4 | - | unknown |
| 0x08009AAE | 0x08009C9E | 496 | A | sub_08009AAE | auto | 0 | 2 | - | unknown |
| 0x08009AB8 | 0x08009AD2 | 26 | A | sub_08009AB8 | auto | 1 | 1 | - | unknown |
| 0x08009AD2 | 0x08009B04 | 50 | A | sub_08009AD2 | auto | 0 | 1 | - | unknown |
| 0x08009B04 | 0x08009B2C | 40 | A | sub_08009B04 | auto | 0 | 3 | - | unknown |
| 0x08009B2C | 0x08009B5E | 50 | A | sub_08009B2C | auto | 1 | 1 | - | unknown |
| 0x08009B30 | 0x08009B5E | 46 | A | sub_08009B30 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009B5E | 0x08009B84 | 38 | A | sub_08009B5E | auto | 0 | 1 | - | unknown |
| 0x08009B84 | 0x08009BB4 | 48 | A | sub_08009B84 | auto | 0 | 1 | - | unknown |
| 0x08009BB4 | 0x08009BE4 | 48 | A | sub_08009BB4 | auto | 0 | 1 | - | unknown |
| 0x08009BE4 | 0x08009C10 | 44 | A | sub_08009BE4 | auto | 0 | 1 | - | unknown |
| 0x08009C10 | 0x08009C30 | 32 | A | sub_08009C10 | auto | 0 | 4 | - | unknown |
| 0x08009C9E | 0x08009CBC | 30 | A | sub_08009C9E | auto | 0 | 0 | - | unknown |
| 0x08009CBC | 0x08009D58 | 156 | A | sub_08009CBC | auto | 2 | 1 | - | unknown |
| 0x08009D58 | 0x08009DFA | 162 | A | sub_08009D58 | auto | 1 | 1 | - | unknown |
| 0x08009DFC | 0x08009E20 | 36 | A | A_scatterload | high | 1 | 1 | - | walks table 0x0800ED54..0x0800ED74 |
| 0x08009E20 | 0x08009E3E | 30 | A | sub_08009E20 | auto | 0 | 1 | - | unknown |
| 0x08009E40 | 0x08009E68 | 40 | A | sub_08009E40 | auto | 2 | 2 | - | unknown |
| 0x08009E44 | 0x08009E62 | 30 | A | sub_08009E44 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009E68 | 0x08009E76 | 14 | A | sub_08009E68 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009E78 | 0x08009E86 | 14 | A | sub_08009E78 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08009E88 | 0x08009E94 | 12 | A | sub_08009E88 | auto | 0 | 1 | - | unknown |
| 0x08009E94 | 0x08009FE8 | 340 | A | sub_08009E94 | auto | 1 | 2 | - | unknown |
| 0x08009FE8 | 0x08009FF2 | 10 | A | sub_08009FE8 | auto | 0 | 2 | - | unknown |
| 0x08009FF2 | 0x0800A03E | 76 | A | sub_08009FF2 | auto | 2 | 1 | - | unknown |
| 0x08010130 | 0x08010144 | 20 | B | B_startup_stub | high | 1 | 0 | - | SP=*(0x08010140)=0x20006C08, bl init-table walker 0x0801DBBC, bx 0x08010145 |
| 0x08010138 | 0x08010140 | 8 | B | sub_08010138 | auto | 0 | 1 | - | unknown |
| 0x08010144 | 0x080101DE | 154 | B | B_main | high | 24 | 0 | - | application entry: init sequence + main loop at 0x080101CC |
| 0x080101DE | 0x080101E8 | 10 | B | sub_080101DE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080101E8 | 0x080101EE | 6 | B | sub_080101E8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080101EE | 0x080102A0 | 178 | B | sub_080101EE | auto | 1 | 0 | - | auto: strings: 'G28 \n'; 'G1 F3000 Z100\n'; 'G1 F6000 X%d Y%d\n\n' / no static callers (dead code or called vi |
| 0x0801030C | 0x08010316 | 10 | B | sub_0801030C | auto | 0 | 0 | SCB | auto: touches SCB / no static callers (dead code or called via pointer) |
| 0x08010316 | 0x08010374 | 94 | B | sub_08010316 | auto | 0 | 2 | SCB | auto: touches SCB |
| 0x08010374 | 0x080103BC | 72 | B | NVIC_SetVectorTable | high | 0 | 1 | SCB | SCB->VTOR = (r0 / r1&0x1FFFFF80); main passes 0x08000000,0x10000 |
| 0x08010382 | 0x080103B8 | 54 | B | sub_08010382 | auto | 0 | 0 | SCB | auto: touches SCB / no static callers (dead code or called via pointer) |
| 0x08010396 | 0x080103AE | 24 | B | sub_08010396 | auto | 0 | 0 | SysTick | auto: touches SysTick / no static callers (dead code or called via pointer) |
| 0x080103BC | 0x080103D4 | 24 | B | sub_080103BC | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080103D4 | 0x080103F8 | 36 | B | sub_080103D4 | auto | 0 | 1 | DAC | auto: touches DAC |
| 0x080103F8 | 0x08010404 | 12 | B | sub_080103F8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010404 | 0x08010418 | 20 | B | sub_08010404 | auto | 0 | 1 | DAC | auto: touches DAC |
| 0x08010418 | 0x0801042C | 20 | B | sub_08010418 | auto | 0 | 0 | DAC | auto: touches DAC / no static callers (dead code or called via pointer) |
| 0x0801042C | 0x08010446 | 26 | B | sub_0801042C | auto | 0 | 0 | DAC | auto: touches DAC / no static callers (dead code or called via pointer) |
| 0x08010446 | 0x0801045E | 24 | B | sub_08010446 | auto | 0 | 0 | DAC | auto: touches DAC / no static callers (dead code or called via pointer) |
| 0x0801045E | 0x08010470 | 18 | B | sub_0801045E | auto | 0 | 0 | DAC | auto: touches DAC / no static callers (dead code or called via pointer) |
| 0x08010470 | 0x080104B8 | 72 | B | sub_08010470 | auto | 0 | 1 | - | unknown |
| 0x08010480 | 0x0801048C | 12 | B | sub_08010480 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801048C | 0x080104B8 | 44 | B | sub_0801048C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080104A4 | 0x080104B4 | 16 | B | sub_080104A4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080104B8 | 0x08010592 | 218 | B | sub_080104B8 | auto | 0 | 0 | DMA1,DMA2 | auto: touches DMA1, DMA2 / no static callers (dead code or called via pointer) |
| 0x08010592 | 0x080105CC | 58 | B | sub_08010592 | auto | 0 | 1 | - | unknown |
| 0x080105CC | 0x080105E6 | 26 | B | sub_080105CC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080105E6 | 0x080105FC | 22 | B | sub_080105E6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080105FC | 0x0801060C | 16 | B | sub_080105FC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010610 | 0x08010616 | 6 | B | sub_08010610 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010616 | 0x08010632 | 28 | B | sub_08010616 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010632 | 0x08010680 | 78 | B | sub_08010632 | auto | 0 | 0 | DMA2,DMA1 | auto: touches DMA2, DMA1 / no static callers (dead code or called via pointer) |
| 0x08010646 | 0x08010680 | 58 | B | sub_08010646 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010662 | 0x08010680 | 30 | B | sub_08010662 | auto | 0 | 0 | DMA2,DMA1 | auto: touches DMA2, DMA1 / no static callers (dead code or called via pointer) |
| 0x08010680 | 0x0801069C | 28 | B | sub_08010680 | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x0801069C | 0x08010708 | 108 | B | EXTI_Init | high | 0 | 0 | EXTI | SPL EXTI_Init; no static callers in dump |
| 0x08010708 | 0x08010716 | 14 | B | sub_08010708 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010716 | 0x08010764 | 78 | B | sub_08010716 | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x08010722 | 0x08010764 | 66 | B | sub_08010722 | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x08010734 | 0x08010764 | 48 | B | sub_08010734 | auto | 0 | 0 | EXTI | auto: touches EXTI / no static callers (dead code or called via pointer) |
| 0x0801073C | 0x08010764 | 40 | B | sub_0801073C | auto | 0 | 1 | EXTI | auto: touches EXTI |
| 0x08010768 | 0x08010776 | 14 | B | sub_08010768 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010776 | 0x08010788 | 18 | B | sub_08010776 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010788 | 0x0801079A | 18 | B | sub_08010788 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x0801079A | 0x080107A6 | 12 | B | sub_0801079A | auto | 0 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x080107A6 | 0x080107B2 | 12 | B | sub_080107A6 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080107B2 | 0x080107BE | 12 | B | sub_080107B2 | auto | 0 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x080107BE | 0x080107CA | 12 | B | sub_080107BE | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080107CA | 0x080107EC | 34 | B | sub_080107CA | auto | 0 | 2 | FLASH_IF | auto: touches FLASH_IF |
| 0x080107EC | 0x0801080E | 34 | B | sub_080107EC | auto | 1 | 9 | - | unknown |
| 0x0801080E | 0x08010846 | 56 | B | sub_0801080E | auto | 1 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x08010846 | 0x0801087A | 52 | B | sub_08010846 | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x0801087A | 0x0801089C | 34 | B | sub_0801087A | auto | 1 | 1 | - | unknown |
| 0x0801089C | 0x080108D0 | 52 | B | sub_0801089C | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080108D0 | 0x080108DE | 14 | B | sub_080108D0 | auto | 0 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x080108DE | 0x0801094A | 108 | B | sub_080108DE | auto | 2 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x0801094A | 0x08010992 | 72 | B | sub_0801094A | auto | 1 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x08010992 | 0x080109C2 | 48 | B | sub_08010992 | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x080109C2 | 0x08010A00 | 62 | B | sub_080109C2 | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010A00 | 0x08010A9E | 158 | B | sub_08010A00 | auto | 1 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x08010A9E | 0x08010B14 | 118 | B | sub_08010A9E | auto | 1 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010B14 | 0x08010B70 | 92 | B | sub_08010B14 | auto | 1 | 0 | FLASH_IF,OptionBytes | auto: touches FLASH_IF, OptionBytes / no static callers (dead code or called via pointer) |
| 0x08010B70 | 0x08010B78 | 8 | B | sub_08010B70 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010B78 | 0x08010B7E | 6 | B | sub_08010B78 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010B7E | 0x08010B8C | 14 | B | sub_08010B7E | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010B8C | 0x08010B9E | 18 | B | sub_08010B8C | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010B9E | 0x08010BE8 | 74 | B | sub_08010B9E | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010BBA | 0x08010BE8 | 46 | B | sub_08010BBA | auto | 0 | 1 | FLASH_IF | auto: touches FLASH_IF |
| 0x08010BC0 | 0x08010BE8 | 40 | B | sub_08010BC0 | auto | 0 | 0 | FLASH_IF | auto: touches FLASH_IF / no static callers (dead code or called via pointer) |
| 0x08010BE8 | 0x08010C0E | 38 | B | sub_08010BE8 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010C0E | 0x08010C36 | 40 | B | sub_08010C0E | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010C36 | 0x08010C50 | 26 | B | sub_08010C36 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010C50 | 0x08010D18 | 200 | B | FSMC_NORSRAMInit | high | 0 | 1 | - | SPL FSMC_NORSRAMInit: BCRx/BTRx/BWTRx |
| 0x08010D18 | 0x08010D80 | 104 | B | FSMC_NANDInit | high | 0 | 1 | FSMC_REGS | SPL FSMC_NANDInit: PCR2/PMEM2/PATT2 |
| 0x08010D80 | 0x08010DE6 | 102 | B | sub_08010D80 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010DE6 | 0x08010E48 | 98 | B | sub_08010DE6 | auto | 0 | 1 | - | unknown |
| 0x08010E48 | 0x08010E7E | 54 | B | sub_08010E48 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010E7E | 0x08010EBA | 60 | B | sub_08010E7E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08010EBA | 0x08010ED4 | 26 | B | FSMC_NORSRAMCmd | medium | 0 | 1 | - | enable bit of BCRx |
| 0x08010ED4 | 0x08010F0A | 54 | B | FSMC_NANDCmd | medium | 0 | 1 | FSMC_REGS | enable bit of PCR2 |
| 0x08010F0A | 0x08010F26 | 28 | B | sub_08010F0A | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010F26 | 0x08010F5C | 54 | B | sub_08010F26 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010F5C | 0x08010F6E | 18 | B | sub_08010F5C | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010F6E | 0x08010FB6 | 72 | B | sub_08010F6E | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010FB6 | 0x08010FDE | 40 | B | sub_08010FB6 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08010FDE | 0x08011004 | 38 | B | sub_08010FDE | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08011004 | 0x08011034 | 48 | B | sub_08011004 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08011034 | 0x0801105E | 42 | B | sub_08011034 | auto | 0 | 0 | FSMC_REGS | auto: touches FSMC_REGS / no static callers (dead code or called via pointer) |
| 0x08011066 | 0x080110FC | 150 | B | sub_08011066 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080110FC | 0x08011112 | 22 | B | sub_080110FC | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011112 | 0x080111AE | 156 | B | GPIO_Init | high | 0 | 9 | - | SPL GPIO_Init; struct {u16 pin;u8 speed;u8 mode}; modes 0x28/0x48 handled via BRR/BSRR |
| 0x080111AE | 0x080111BE | 16 | B | sub_080111AE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080111BE | 0x080111CC | 14 | B | GPIO_ReadInputDataBit | medium | 0 | 9 | - | returns (GPIOx->IDR & pin)!=0 |
| 0x080111CC | 0x080111D2 | 6 | B | sub_080111CC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080111D2 | 0x080111E0 | 14 | B | sub_080111D2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080111E0 | 0x080111E6 | 6 | B | sub_080111E0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080111E6 | 0x080111EA | 4 | B | GPIO_SetBits | high | 0 | 17 | - | GPIOx->BSRR = pins |
| 0x080111EA | 0x080111EE | 4 | B | GPIO_ResetBits | high | 0 | 23 | - | GPIOx->BRR = pins |
| 0x080111EE | 0x080111F8 | 10 | B | sub_080111EE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080111FC | 0x0801120C | 16 | B | sub_080111FC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801120E | 0x08011222 | 20 | B | sub_0801120E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011222 | 0x08011228 | 6 | B | sub_08011222 | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x08011228 | 0x0801127A | 82 | B | sub_08011228 | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x0801127A | 0x080112C4 | 74 | B | sub_0801127A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801129C | 0x080112C8 | 44 | B | sub_0801129C | auto | 0 | 0 | AFIO | auto: touches AFIO / no static callers (dead code or called via pointer) |
| 0x080112C8 | 0x080112FA | 50 | B | sub_080112C8 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080112FA | 0x0801132A | 48 | B | sub_080112FA | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801132A | 0x08011354 | 42 | B | sub_0801132A | auto | 0 | 1 | RCC | auto: touches RCC |
| 0x08011354 | 0x08011380 | 44 | B | sub_08011354 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011380 | 0x08011390 | 16 | B | sub_08011380 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011390 | 0x08011396 | 6 | B | sub_08011390 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011396 | 0x080113A6 | 16 | B | sub_08011396 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113A6 | 0x080113AC | 6 | B | sub_080113A6 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113AC | 0x080113BA | 14 | B | sub_080113AC | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113BA | 0x080113C4 | 10 | B | sub_080113BA | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113C4 | 0x080113D2 | 14 | B | sub_080113C4 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113D2 | 0x080113E0 | 14 | B | sub_080113D2 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113E0 | 0x080113F0 | 16 | B | sub_080113E0 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x080113F0 | 0x08011402 | 18 | B | sub_080113F0 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011402 | 0x0801140A | 8 | B | sub_08011402 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801140A | 0x08011418 | 14 | B | sub_0801140A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011418 | 0x08011434 | 28 | B | sub_08011418 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011434 | 0x0801143A | 6 | B | sub_08011434 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801143A | 0x08011444 | 10 | B | sub_0801143A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011444 | 0x0801144C | 8 | B | sub_08011444 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801144C | 0x080114D0 | 132 | B | sub_0801144C | auto | 0 | 2 | RCC | auto: touches RCC |
| 0x080114D0 | 0x080114E2 | 18 | B | RCC_AHBPeriphClockCmd | medium | 0 | 3 | RCC | RCC->AHBENR set/clear (FSMC clock = 0x100) |
| 0x080114E2 | 0x080114F4 | 18 | B | RCC_APB2PeriphClockCmd | high | 0 | 9 | RCC | RCC->APB2ENR set/clear |
| 0x080114F4 | 0x08011506 | 18 | B | RCC_APB1PeriphClockCmd | high | 0 | 4 | RCC | RCC->APB1ENR set/clear |
| 0x08011506 | 0x08011518 | 18 | B | sub_08011506 | auto | 0 | 5 | RCC | auto: touches RCC |
| 0x08011518 | 0x08011564 | 76 | B | sub_08011518 | auto | 0 | 4 | RCC | auto: touches RCC |
| 0x0801152A | 0x08011574 | 74 | B | sub_0801152A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011532 | 0x08011570 | 62 | B | sub_08011532 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011538 | 0x08011564 | 44 | B | sub_08011538 | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801153E | 0x08011564 | 38 | B | sub_0801153E | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801154A | 0x08011564 | 26 | B | sub_0801154A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x0801155A | 0x08011564 | 10 | B | sub_0801155A | auto | 0 | 0 | RCC | auto: touches RCC / no static callers (dead code or called via pointer) |
| 0x08011582 | 0x080115C8 | 70 | B | sub_08011582 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080115C8 | 0x08011600 | 56 | B | sub_080115C8 | auto | 0 | 2 | - | unknown |
| 0x08011600 | 0x08011696 | 150 | B | sub_08011600 | auto | 1 | 1 | - | unknown |
| 0x08011696 | 0x080116AE | 24 | B | sub_08011696 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080116AE | 0x080116C0 | 18 | B | sub_080116AE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080116C0 | 0x080116D4 | 20 | B | sub_080116C0 | auto | 0 | 2 | - | unknown |
| 0x080116D4 | 0x080116E8 | 20 | B | sub_080116D4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080116E8 | 0x08011700 | 24 | B | sub_080116E8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011700 | 0x08011710 | 16 | B | sub_08011700 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011718 | 0x08011730 | 24 | B | sub_08011718 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011730 | 0x08011744 | 20 | B | sub_08011730 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011744 | 0x08011754 | 16 | B | sub_08011744 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011754 | 0x0801175E | 10 | B | sub_08011754 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801175E | 0x08011772 | 20 | B | sub_0801175E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011772 | 0x0801177E | 12 | B | sub_08011772 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011782 | 0x08011798 | 22 | B | sub_08011782 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011798 | 0x080117A6 | 14 | B | sub_08011798 | auto | 0 | 1 | - | unknown |
| 0x080117A6 | 0x080117AC | 6 | B | sub_080117A6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080117AC | 0x080117D8 | 44 | B | sub_080117AC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080117D8 | 0x080117E6 | 14 | B | sub_080117D8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080117F6 | 0x08011924 | 302 | B | sub_080117F6 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011924 | 0x08011996 | 114 | B | sub_08011924 | auto | 0 | 1 | - | unknown |
| 0x08011996 | 0x08011A00 | 106 | B | sub_08011996 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011A00 | 0x08011A78 | 120 | B | sub_08011A00 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011A78 | 0x08011AEC | 116 | B | sub_08011A78 | auto | 0 | 1 | - | unknown |
| 0x08011AEC | 0x08011B46 | 90 | B | sub_08011AEC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011B46 | 0x08011B5E | 24 | B | sub_08011B46 | auto | 0 | 0 | - | unknown |
| 0x08011B5E | 0x08011B6E | 16 | B | sub_08011B5E | auto | 0 | 0 | - | unknown |
| 0x08011B6E | 0x08011B86 | 24 | B | sub_08011B6E | auto | 0 | 1 | - | unknown |
| 0x08011B86 | 0x08011C2C | 166 | B | sub_08011B86 | auto | 0 | 3 | - | unknown |
| 0x08011C2C | 0x08011C3C | 16 | B | sub_08011C2C | auto | 0 | 1 | - | unknown |
| 0x08011C3C | 0x08011C94 | 88 | B | sub_08011C3C | auto | 0 | 3 | - | unknown |
| 0x08011C94 | 0x08011DA2 | 270 | B | sub_08011C94 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011DA2 | 0x08011E0A | 104 | B | sub_08011DA2 | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E0A | 0x08011E2C | 34 | B | sub_08011E0A | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E2C | 0x08011E3E | 18 | B | sub_08011E2C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E3E | 0x08011E52 | 20 | B | sub_08011E3E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E52 | 0x08011E62 | 16 | B | sub_08011E52 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E62 | 0x08011E74 | 18 | B | sub_08011E62 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E74 | 0x08011E88 | 20 | B | sub_08011E74 | auto | 0 | 1 | - | unknown |
| 0x08011E88 | 0x08011E9E | 22 | B | sub_08011E88 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011E9E | 0x08011EAE | 16 | B | sub_08011E9E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011EB2 | 0x08011EBA | 8 | B | sub_08011EB2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011EBA | 0x08011ECA | 16 | B | sub_08011EBA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011ECA | 0x08011ED4 | 10 | B | sub_08011ECA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011ED4 | 0x08011EE0 | 12 | B | sub_08011ED4 | auto | 0 | 2 | - | unknown |
| 0x08011EE0 | 0x08011EF2 | 18 | B | sub_08011EE0 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011EF2 | 0x08011F20 | 46 | B | sub_08011EF2 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011F20 | 0x08011F38 | 24 | B | sub_08011F20 | auto | 0 | 2 | - | unknown |
| 0x08011F38 | 0x08011F4A | 18 | B | sub_08011F38 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011F4A | 0x08011F5C | 18 | B | sub_08011F4A | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011F5C | 0x08011F62 | 6 | B | sub_08011F5C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011F62 | 0x08011F6E | 12 | B | sub_08011F62 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011F6E | 0x08011FA0 | 50 | B | sub_08011F6E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011FA0 | 0x08011FAC | 12 | B | sub_08011FA0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011FAC | 0x08011FC0 | 20 | B | sub_08011FAC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011FC0 | 0x08011FCC | 12 | B | sub_08011FC0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011FCC | 0x08011FE0 | 20 | B | sub_08011FCC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011FE0 | 0x08011FF4 | 20 | B | sub_08011FE0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08011FF4 | 0x08012008 | 20 | B | sub_08011FF4 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012008 | 0x0801201C | 20 | B | sub_08012008 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801201C | 0x08012030 | 20 | B | sub_0801201C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012064 | 0x08012070 | 12 | B | sub_08012064 | auto | 0 | 1 | - | unknown |
| 0x08012180 | 0x08012196 | 22 | B | sub_08012180 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012196 | 0x080121AC | 22 | B | sub_08012196 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080121AC | 0x080121F2 | 70 | B | sub_080121AC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080122E4 | 0x08012344 | 96 | B | sub_080122E4 | auto | 2 | 1 | - | unknown |
| 0x08012344 | 0x080123EA | 166 | B | sub_08012344 | auto | 1 | 1 | - | unknown |
| 0x080123EA | 0x08012400 | 22 | B | sub_080123EA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012400 | 0x0801241E | 30 | B | sub_08012400 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801241E | 0x0801242A | 12 | B | sub_0801241E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801242A | 0x0801243E | 20 | B | sub_0801242A | auto | 0 | 1 | - | unknown |
| 0x0801243E | 0x0801246E | 48 | B | sub_0801243E | auto | 0 | 1 | - | unknown |
| 0x0801246E | 0x0801247E | 16 | B | sub_0801246E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801247E | 0x0801248E | 16 | B | sub_0801247E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801248E | 0x0801249E | 16 | B | sub_0801248E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801249E | 0x080124B2 | 20 | B | sub_0801249E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080124B2 | 0x080124C2 | 16 | B | sub_080124B2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080124C2 | 0x080124D6 | 20 | B | sub_080124C2 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080124D6 | 0x080124DE | 8 | B | sub_080124D6 | auto | 0 | 1 | - | unknown |
| 0x080124DE | 0x080124E6 | 8 | B | sub_080124DE | auto | 0 | 1 | - | unknown |
| 0x080124E6 | 0x080124F0 | 10 | B | sub_080124E6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080124F0 | 0x08012500 | 16 | B | sub_080124F0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012500 | 0x08012510 | 16 | B | sub_08012500 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012510 | 0x08012524 | 20 | B | sub_08012510 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012524 | 0x08012538 | 20 | B | sub_08012524 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012538 | 0x0801254C | 20 | B | sub_08012538 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801254C | 0x08012560 | 20 | B | sub_0801254C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012560 | 0x08012574 | 20 | B | sub_08012560 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012574 | 0x08012584 | 16 | B | sub_08012574 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012584 | 0x08012598 | 20 | B | sub_08012584 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08012598 | 0x080125A6 | 14 | B | sub_08012598 | auto | 0 | 1 | - | unknown |
| 0x080125A6 | 0x080125AC | 6 | B | sub_080125A6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080125AC | 0x080125EA | 62 | B | sub_080125AC | auto | 0 | 1 | - | unknown |
| 0x080125EA | 0x080125F6 | 12 | B | sub_080125EA | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801260C | 0x0801260E | 2 | B | sub_0801260C | auto | 0 | 0 | - | unknown |
| 0x0801260E | 0x08012610 | 2 | B | sub_0801260E | auto | 0 | 0 | - | unknown |
| 0x08012610 | 0x08012612 | 2 | B | sub_08012610 | auto | 0 | 0 | - | unknown |
| 0x08012612 | 0x08012614 | 2 | B | sub_08012612 | auto | 0 | 0 | - | unknown |
| 0x08012614 | 0x08012616 | 2 | B | sub_08012614 | auto | 0 | 0 | - | unknown |
| 0x08012616 | 0x08012618 | 2 | B | sub_08012616 | auto | 0 | 0 | - | unknown |
| 0x08012618 | 0x0801261A | 2 | B | sub_08012618 | auto | 0 | 0 | - | unknown |
| 0x0801261A | 0x0801261C | 2 | B | sub_0801261A | auto | 0 | 0 | - | unknown |
| 0x0801261C | 0x0801261E | 2 | B | sub_0801261C | auto | 0 | 0 | - | unknown |
| 0x08012620 | 0x08012634 | 20 | B | sub_08012620 | auto | 1 | 2 | - | unknown |
| 0x08012634 | 0x0801263C | 8 | B | sub_08012634 | auto | 0 | 2 | - | unknown |
| 0x0801263C | 0x08012664 | 40 | B | sub_0801263C | auto | 2 | 5 | - | unknown |
| 0x08012664 | 0x0801268C | 40 | B | sub_08012664 | auto | 2 | 5 | - | unknown |
| 0x0801268C | 0x080126E4 | 88 | B | sub_0801268C | auto | 4 | 1 | - | unknown |
| 0x080126DC | 0x080126E0 | 4 | B | sub_080126DC | auto | 0 | 3 | - | unknown |
| 0x080126E4 | 0x0801274E | 106 | B | sub_080126E4 | auto | 2 | 13 | - | unknown |
| 0x0801274E | 0x08012804 | 182 | B | sub_0801274E | auto | 4 | 5 | - | unknown |
| 0x08012804 | 0x080128BC | 184 | B | sub_08012804 | auto | 1 | 8 | - | unknown |
| 0x080128BC | 0x080129AE | 242 | B | sub_080128BC | auto | 1 | 3 | - | unknown |
| 0x080129AE | 0x08012A0E | 96 | B | sub_080129AE | auto | 2 | 4 | - | unknown |
| 0x08012A0E | 0x08012AA2 | 148 | B | sub_08012A0E | auto | 2 | 3 | - | unknown |
| 0x08012AA2 | 0x08012B14 | 114 | B | sub_08012AA2 | auto | 2 | 7 | - | unknown |
| 0x08012B14 | 0x08012C02 | 238 | B | sub_08012B14 | auto | 5 | 5 | - | unknown |
| 0x08012C02 | 0x08012C6E | 108 | B | sub_08012C02 | auto | 1 | 1 | - | unknown |
| 0x08012C6E | 0x08012D84 | 278 | B | sub_08012C6E | auto | 5 | 2 | - | unknown |
| 0x08012D84 | 0x08012E5C | 216 | B | sub_08012D84 | auto | 3 | 2 | - | unknown |
| 0x08012E5C | 0x08013000 | 420 | B | sub_08012E5C | auto | 8 | 3 | - | unknown |
| 0x08013000 | 0x0801304E | 78 | B | sub_08013000 | auto | 3 | 2 | - | unknown |
| 0x0801304E | 0x08013214 | 454 | B | sub_0801304E | auto | 3 | 1 | - | auto: strings: '+,;[=]' |
| 0x08013214 | 0x080132DA | 198 | B | sub_08013214 | auto | 1 | 2 | - | unknown |
| 0x080132DA | 0x08013354 | 122 | B | sub_080132DA | auto | 3 | 8 | - | unknown |
| 0x08013354 | 0x080133AA | 86 | B | sub_08013354 | auto | 2 | 1 | - | auto: strings: 'FAT'; 'FAT32' |
| 0x080133AA | 0x08013588 | 478 | B | sub_080133AA | auto | 4 | 9 | - | unknown |
| 0x08013588 | 0x080135A4 | 28 | B | sub_08013588 | auto | 0 | 1 | - | unknown |
| 0x080135A4 | 0x080136F0 | 332 | B | sub_080135A4 | auto | 6 | 4 | - | unknown |
| 0x080136F0 | 0x08013824 | 308 | B | sub_080136F0 | auto | 6 | 6 | - | unknown |
| 0x0801399A | 0x08013A3E | 164 | B | sub_0801399A | auto | 4 | 1 | - | unknown |
| 0x08013A3E | 0x08013A50 | 18 | B | sub_08013A3E | auto | 1 | 3 | - | unknown |
| 0x08013A50 | 0x08013B92 | 322 | B | sub_08013A50 | auto | 6 | 5 | - | unknown |
| 0x08013B92 | 0x08013BFE | 108 | B | sub_08013B92 | auto | 3 | 1 | - | unknown |
| 0x08013BFE | 0x08013C5A | 92 | B | sub_08013BFE | auto | 5 | 1 | - | unknown |
| 0x08013C5A | 0x08013C9C | 66 | B | sub_08013C5A | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08013C9C | 0x08013D2C | 144 | B | sub_08013C9C | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08013D2C | 0x08013DE8 | 188 | B | sub_08013D2C | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08013DE8 | 0x08013E80 | 152 | B | sub_08013DE8 | auto | 8 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08013E80 | 0x08014014 | 404 | B | sub_08013E80 | auto | 11 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08014014 | 0x08014068 | 84 | B | sub_08014014 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08014068 | 0x080140C0 | 88 | B | sub_08014068 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080140C0 | 0x080141B8 | 248 | B | sub_080140C0 | auto | 8 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080141B8 | 0x080141C8 | 16 | B | sub_080141B8 | auto | 0 | 6 | - | unknown |
| 0x080141C8 | 0x080141D6 | 14 | B | sub_080141C8 | auto | 0 | 5 | - | unknown |
| 0x080141D6 | 0x080141EE | 24 | B | sub_080141D6 | auto | 0 | 2 | - | unknown |
| 0x080141EE | 0x080141FE | 16 | B | sub_080141EE | auto | 0 | 1 | - | unknown |
| 0x080141FE | 0x08014216 | 24 | B | sub_080141FE | auto | 0 | 6 | - | unknown |
| 0x08014216 | 0x08014230 | 26 | B | sub_08014216 | auto | 0 | 3 | - | unknown |
| 0x08014230 | 0x08014250 | 32 | B | sub_08014230 | auto | 1 | 5 | - | unknown |
| 0x08014250 | 0x0801437C | 300 | B | SD_ReadConfig_or_Index | low | 7 | 1 | - | called after SD_Init success; uses buffers 0x200033F4/0x20003654 and tick |
| 0x0801437C | 0x080143D0 | 84 | B | sub_0801437C | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080143D0 | 0x08014434 | 100 | B | sub_080143D0 | auto | 3 | 1 | - | unknown |
| 0x08014434 | 0x08014490 | 92 | B | sub_08014434 | auto | 3 | 1 | - | unknown |
| 0x08014490 | 0x080144F0 | 96 | B | sub_08014490 | auto | 3 | 1 | - | unknown |
| 0x08014508 | 0x08014516 | 14 | B | sub_08014508 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08014518 | 0x0801454C | 52 | B | sub_08014518 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801454C | 0x0801455A | 14 | B | sub_0801454C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801455A | 0x080145CA | 112 | B | sub_0801455A | auto | 5 | 1 | - | unknown |
| 0x080145CA | 0x0801466C | 162 | B | sub_080145CA | auto | 5 | 1 | - | unknown |
| 0x0801466C | 0x08014702 | 150 | B | sub_0801466C | auto | 5 | 1 | - | unknown |
| 0x08014702 | 0x080147A2 | 160 | B | SD_to_NAND_Loader | medium | 6 | 1 | - | prints "Loading...: %d/%d" |
| 0x080147F0 | 0x0801484E | 94 | B | sub_080147F0 | auto | 4 | 1 | - | unknown |
| 0x0801484E | 0x080148EA | 156 | B | sub_0801484E | auto | 5 | 2 | - | unknown |
| 0x080148EA | 0x08014946 | 92 | B | Show_NAND_Image | high | 4 | 2 | - | image n at NAND byte offset n*3*0x20000; 150 pages x 1024 px (=480*320 RGB565) to LCD window 0..0x1DF,0..0x13F |
| 0x08014946 | 0x08014964 | 30 | B | Show_All_Images_Test | medium | 1 | 2 | - | loops images 0..0x3C then waits 3000 ticks |
| 0x08014964 | 0x08014974 | 16 | B | sub_08014964 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08014A38 | 0x08014A8C | 84 | B | sub_08014A38 | auto | 0 | 2 | - | unknown |
| 0x08014A6C | 0x08014A94 | 40 | B | sub_08014A6C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08014A94 | 0x08014AAE | 26 | B | sub_08014A94 | auto | 0 | 5 | - | unknown |
| 0x08014AAE | 0x08014AC8 | 26 | B | sub_08014AAE | auto | 0 | 7 | - | unknown |
| 0x08014AC8 | 0x08014B92 | 202 | B | SD_SPI2_Init | high | 6 | 1 | - | SPI2 clk, PB13/14/15 AF/PB12 out/PB11 card-detect, SPI_Init struct master, soft NSS, prescaler 0x38 |
| 0x08014B92 | 0x08014BE8 | 86 | B | SD_SetSpeed | medium | 2 | 5 | - | SPI2 prescaler change (called with 1 after init) |
| 0x08014BE8 | 0x08014C12 | 42 | B | SD_SPI_ReadWriteByte | high | 1 | 8 | SPI2 | wait TXE, SPI2->DR=r0, wait RXNE, return DR |
| 0x08014C12 | 0x08014C94 | 130 | B | SD_SendCmd | medium | 5 | 6 | - | send command frame (cmd, arg, crc) and poll R1 |
| 0x08014C94 | 0x08014CFA | 102 | B | sub_08014C94 | auto | 4 | 1 | - | unknown |
| 0x08014CFA | 0x08014E96 | 412 | B | SD_Init | high | 8 | 2 | - | CMD0(crc 0x95), CMD8(0x1AA,crc 0x87), ACMD41 (CMD55+CMD41), CMD1 fallback, CMD58, CMD16(0x200), speed-up |
| 0x08014E96 | 0x08014F12 | 124 | B | sub_08014E96 | auto | 5 | 2 | - | unknown |
| 0x08014F12 | 0x08014F44 | 50 | B | sub_08014F12 | auto | 2 | 1 | - | unknown |
| 0x08014F44 | 0x08014FA8 | 100 | B | sub_08014F44 | auto | 6 | 1 | - | unknown |
| 0x08014FA8 | 0x0801507E | 214 | B | sub_08014FA8 | auto | 7 | 1 | - | unknown |
| 0x0801507E | 0x0801509C | 30 | B | sub_0801507E | auto | 1 | 2 | - | unknown |
| 0x0801509C | 0x080150BC | 32 | B | sub_0801509C | auto | 2 | 1 | - | unknown |
| 0x080150BC | 0x0801514C | 144 | B | sub_080150BC | auto | 1 | 1 | - | unknown |
| 0x0801514C | 0x08015234 | 232 | B | sub_0801514C | auto | 8 | 1 | - | unknown |
| 0x08015234 | 0x0801523C | 8 | B | sub_08015234 | auto | 0 | 1 | - | unknown |
| 0x0801523C | 0x08015252 | 22 | B | sub_0801523C | auto | 0 | 2 | - | unknown |
| 0x08015252 | 0x0801527A | 40 | B | LCD_Reset | high | 3 | 1 | - | PE5 low, delay 400, PE5 high, delay 400 (software delay 0x080164DC) |
| 0x0801527A | 0x08015282 | 8 | B | sub_0801527A | auto | 0 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x08015282 | 0x08015288 | 6 | B | sub_08015282 | auto | 0 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x08015288 | 0x0801528E | 6 | B | sub_08015288 | auto | 0 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x0801528E | 0x08015294 | 6 | B | sub_0801528E | auto | 0 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x08015294 | 0x080152D2 | 62 | B | sub_08015294 | auto | 0 | 2 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x080152D2 | 0x080152E6 | 20 | B | sub_080152D2 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080152E6 | 0x080152EE | 8 | B | sub_080152E6 | auto | 0 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x080152EE | 0x08015320 | 50 | B | LCD_SetWindow | high | 0 | 6 | FSMC_BANK1(NOR/SRAM/LCD) | CMD 2A (x0=r0,x1=r2), CMD 2B (y0=r1,y1=r3) |
| 0x08015320 | 0x0801537C | 92 | B | sub_08015320 | auto | 1 | 1 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x0801537C | 0x080153BC | 64 | B | sub_0801537C | auto | 2 | 5 | - | unknown |
| 0x080153BC | 0x080153E4 | 40 | B | sub_080153BC | auto | 2 | 0 | - | auto: strings: '%d %d' / no static callers (dead code or called via pointer) |
| 0x080153E4 | 0x080154D4 | 240 | B | LCD_GPIO_FSMC_Init | high | 7 | 1 | - | GPIO for LCD bus (PD/PE AF_PP, PE3/PE5 out, PC9 out) + FSMC Bank1 config |
| 0x080154D4 | 0x08015522 | 78 | B | LCD_FillRect | low | 2 | 10 | FSMC_BANK1(NOR/SRAM/LCD) | window + pixel fill (user-supplied; not re-verified) |
| 0x08015522 | 0x0801555A | 56 | B | LCD_Clear | medium | 2 | 1 | - | fill screen (called from LCD_Init) |
| 0x0801555A | 0x080156D4 | 378 | B | LCD_Init_ILI9488 | high | 7 | 1 | FSMC_BANK1(NOR/SRAM/LCD) | reset, CS low, command stream E0,E1,C0,C1,C5,36,3A,B0,B1,B4,B6,E9,F7,20,11,29,2C, clear, backlight PC9 |
| 0x080156D4 | 0x080156FE | 42 | B | sub_080156D4 | auto | 0 | 3 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x080156FE | 0x0801574C | 78 | B | sub_080156FE | auto | 1 | 3 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x0801574C | 0x08015780 | 52 | B | sub_0801574C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08015784 | 0x080157E0 | 92 | B | sub_08015784 | auto | 1 | 1 | - | unknown |
| 0x080157E0 | 0x0801581A | 58 | B | sub_080157E0 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801581A | 0x08015870 | 86 | B | LCD_SetWindow_Wrapper | medium | 1 | 3 | FSMC_BANK1(NOR/SRAM/LCD) | called with (0,0,0x1DF,0x13F) = full 480x320 screen |
| 0x08015870 | 0x080158C2 | 82 | B | sub_08015870 | auto | 2 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x080158C2 | 0x08015914 | 82 | B | sub_080158C2 | auto | 2 | 2 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x08015914 | 0x08015940 | 44 | B | LCD_WriteBuffer | medium | 1 | 3 | - | writes r0 pixels from buffer r1 to LCD (called with 0x400 pixels per NAND page) |
| 0x08015940 | 0x08015974 | 52 | B | sub_08015940 | auto | 1 | 0 | - | unknown |
| 0x08015974 | 0x080159AE | 58 | B | sub_08015974 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080159AE | 0x080159D4 | 38 | B | sub_080159AE | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080159D4 | 0x080159EE | 26 | B | sub_080159D4 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080159F0 | 0x08015A38 | 72 | B | sub_080159F0 | auto | 1 | 2 | - | unknown |
| 0x08015A38 | 0x08015B16 | 222 | B | sub_08015A38 | auto | 4 | 0 | - | auto: strings: 'CANCE' / no static callers (dead code or called via pointer) |
| 0x08015B16 | 0x08015B52 | 60 | B | sub_08015B16 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08015B52 | 0x08015BA6 | 84 | B | sub_08015B52 | auto | 1 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x08015BA6 | 0x08015BCE | 40 | B | sub_08015BA6 | auto | 1 | 0 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) / no static callers (dead code or called via pointer) |
| 0x08015BD0 | 0x08015D0C | 316 | B | sub_08015BD0 | auto | 1 | 1 | - | unknown |
| 0x08015D0C | 0x08015D24 | 24 | B | sub_08015D0C | auto | 1 | 1 | - | unknown |
| 0x08015D24 | 0x08015D46 | 34 | B | sub_08015D24 | auto | 1 | 1 | - | unknown |
| 0x08015D46 | 0x08015D68 | 34 | B | sub_08015D46 | auto | 1 | 1 | - | unknown |
| 0x08015D68 | 0x08015D90 | 40 | B | sub_08015D68 | auto | 1 | 1 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x08015D90 | 0x08015E72 | 226 | B | sub_08015D90 | auto | 2 | 1 | - | unknown |
| 0x08015E72 | 0x08015F0A | 152 | B | sub_08015E72 | auto | 1 | 1 | - | unknown |
| 0x08015F0A | 0x080160C2 | 440 | B | sub_08015F0A | auto | 4 | 3 | - | unknown |
| 0x080161B0 | 0x08016272 | 194 | B | sub_080161B0 | auto | 2 | 2 | - | unknown |
| 0x08016272 | 0x08016386 | 276 | B | sub_08016272 | auto | 5 | 1 | FSMC_BANK1(NOR/SRAM/LCD) | auto: touches FSMC_BANK1(NOR/SRAM/LCD) |
| 0x08016386 | 0x080163AE | 40 | B | sub_08016386 | auto | 2 | 5 | - | unknown |
| 0x080163AE | 0x080163DE | 48 | B | sub_080163AE | auto | 1 | 8 | - | unknown |
| 0x080163DE | 0x080164DC | 254 | B | sub_080163DE | auto | 5 | 3 | - | unknown |
| 0x080164DC | 0x08016510 | 52 | B | delay_soft | high | 0 | 3 | - | busy-wait: r0 x (200 iterations of a RAM read/modify loop); not time-calibrated |
| 0x08016510 | 0x08016578 | 104 | B | XPT2046_SPI_Transfer_bitbang | high | 4 | 1 | - | software SPI byte: SCK=PA5, MOSI=PA7, MISO=PA6, MSB first |
| 0x08016578 | 0x080165C6 | 78 | B | XPT2046_ReadADC | high | 3 | 1 | - | CS=PC4 low, send cmd, read 12 bit (>>4), CS high |
| 0x080165C6 | 0x0801662A | 100 | B | XPT2046_Read_Filtered | high | 1 | 1 | - | 30 x XPT2046_ReadADC(cmd) (0x080165D2..0x080165E0), ascending exchange sort (0x080165EA..0x08016604), mean of  |
| 0x0801662A | 0x08016652 | 40 | B | XPT2046_ReadXY_raw | high | 1 | 4 | - | X=ReadFiltered(0xD0), Y=ReadFiltered(0x90); returns 1 and stores both (u16*) only if both >= 10, else 0 |
| 0x08016652 | 0x080166CE | 124 | B | sub_08016652 | auto | 1 | 2 | - | unknown |
| 0x080166D0 | 0x080166F6 | 38 | B | sub_080166D0 | auto | 2 | 1 | - | unknown |
| 0x080166F6 | 0x080166FE | 8 | B | sub_080166F6 | auto | 0 | 1 | - | unknown |
| 0x080166FC | 0x08016A2C | 816 | B | sub_080166FC | auto | 18 | 0 | - | auto: strings: 'Touch Screen Adjust OK!' / no static callers (dead code or called via pointer) |
| 0x08016A2C | 0x08016ABA | 142 | B | Touch_GPIO_Init | high | 3 | 1 | - | PC4 out, PA5/PA7 out, PA6 IPU, PC5 IPU, then PC4 IPU(!); then one XPT2046_ReadXY_raw 0x0801662A |
| 0x08016ABA | 0x08016AD4 | 26 | B | EXTI4_IRQHandler_vestigial | high | 1 | 0 | EXTI | tests EXTI line5 (0x20) and sets flag 0x200048A4; EXTI_Init has no callers -> never enabled |
| 0x08016AD4 | 0x08016B2A | 86 | B | sub_08016AD4 | auto | 6 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08016B34 | 0x08016B46 | 18 | B | sub_08016B34 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08016B46 | 0x08016BB0 | 106 | B | sub_08016B46 | auto | 5 | 1 | - | unknown |
| 0x08016BB0 | 0x08016C74 | 196 | B | Touch_Poll | medium | 7 | 0 | - | reads PENIRQ PC5 (GPIOC pin 0x20), delays, XPT2046 read, float scaling (const 0x40733333/0x40B33333) |
| 0x08016C74 | 0x08016D26 | 178 | B | sub_08016C74 | auto | 4 | 21 | - | unknown |
| 0x08016DF0 | 0x08016E10 | 32 | B | sub_08016DF0 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08016E10 | 0x08016E20 | 16 | B | sub_08016E10 | auto | 0 | 2 | - | unknown |
| 0x08016E20 | 0x08016E52 | 50 | B | sub_08016E20 | auto | 1 | 1 | - | unknown |
| 0x08016E52 | 0x08016E86 | 52 | B | sub_08016E52 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08016E86 | 0x08016EB2 | 44 | B | sub_08016E86 | auto | 0 | 8 | - | unknown |
| 0x08016EB2 | 0x08016EFC | 74 | B | sub_08016EB2 | auto | 0 | 19 | - | unknown |
| 0x08016EE0 | 0x08016EF8 | 24 | B | sub_08016EE0 | auto | 0 | 1 | - | unknown |
| 0x08016EFC | 0x08016F82 | 134 | B | sub_08016EFC | auto | 0 | 1 | - | unknown |
| 0x08016F82 | 0x08016FE6 | 100 | B | sub_08016F82 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08016FE6 | 0x08017086 | 160 | B | sub_08016FE6 | auto | 4 | 1 | - | unknown |
| 0x08017086 | 0x08017144 | 190 | B | sub_08017086 | auto | 2 | 4 | - | unknown |
| 0x08017144 | 0x08017198 | 84 | B | sub_08017144 | auto | 1 | 6 | - | unknown |
| 0x08017168 | 0x08017198 | 48 | B | sub_08017168 | auto | 1 | 3 | - | unknown |
| 0x08017198 | 0x080171F0 | 88 | B | SysTick_Config_unused | high | 0 | 0 | SysTick,SCB | LOAD=SystemCoreClock/1000-1, prio 0xF0, CTRL=7; no static callers |
| 0x080171C6 | 0x080171F4 | 46 | B | sub_080171C6 | auto | 0 | 2 | - | unknown |
| 0x080171D6 | 0x080171F4 | 30 | B | sub_080171D6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080171F4 | 0x08017222 | 46 | B | sub_080171F4 | auto | 2 | 1 | - | unknown |
| 0x08017222 | 0x0801723A | 24 | B | sub_08017222 | auto | 0 | 1 | GPIOE | auto: touches GPIOE |
| 0x0801723A | 0x0801728C | 82 | B | sub_0801723A | auto | 2 | 1 | GPIOE | auto: touches GPIOE |
| 0x0801728C | 0x080172C4 | 56 | B | TIM2_Tick_Init | high | 0 | 1 | RCC,TIM2,NVIC | TIM2: PSC=r0 ARR=r1 UIE+CEN, NVIC ISER0 bit28; main calls with PSC=0x47 ARR=0x3E7 |
| 0x080172C4 | 0x08017340 | 124 | B | TIM2_IRQHandler | high | 1 | 0 | TIM2 | clears UIF; ++tick(0x20000070), ++0x2000006C; countdown 0x20000074 -> calls 0x080175A6 (buzzer off) |
| 0x08017300 | 0x08017340 | 64 | B | sub_08017300 | auto | 0 | 29 | - | unknown |
| 0x08017306 | 0x08017340 | 58 | B | tick_elapsed | high | 0 | 4 | - | returns tick_counter(0x20000070) - r0 |
| 0x0801730E | 0x08017340 | 50 | B | delay_ms_tim2 | high | 1 | 2 | - | waits until TIM2 tick counter (RAM 0x20000070) advanced by r0 ticks |
| 0x08017322 | 0x08017348 | 38 | B | sub_08017322 | auto | 0 | 2 | - | unknown |
| 0x08017348 | 0x08017366 | 30 | B | sub_08017348 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08017366 | 0x0801738A | 36 | B | uart_rx_push | high | 0 | 1 | - | ring buf 0x200048B4 (250 bytes), idx 0x20000078, counts LF into 0x2000007C |
| 0x0801738A | 0x0801744A | 192 | B | USART1_Init_115200 | high | 8 | 1 | - | PA9 AF_PP, PA10 IPU, PA8 out(reset line), USART1 115200 8N1 TX+RX, RXNE IRQ, NVIC |
| 0x0801744A | 0x08017462 | 24 | B | uart_putc | high | 0 | 1 | USART1 | USART1->DR=c; wait TC (bit6); clear TC |
| 0x08017462 | 0x08017476 | 20 | B | sub_08017462 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08017476 | 0x0801749E | 40 | B | USART1_IRQHandler | high | 3 | 0 | - | RXNE -> read DR -> ring buffer push 0x08017366 |
| 0x0801749E | 0x0801751C | 126 | B | uart_get_line | high | 0 | 1 | - | pops one LF-terminated line (<=0x78 chars); empty/CR-only line returns "OK0" |
| 0x08017520 | 0x080175C0 | 160 | B | Buzzer_TIM5_PWM_Init | high | 7 | 1 | TIM5 | PA2 AF_PP, TIM5 base ARR=0x31F, PSC=r1, PWM mode 0x70 on CH3, CCR3 preload; main calls (0,0x28) |
| 0x080175A6 | 0x080175C0 | 26 | B | Buzzer_Off | low | 0 | 2 | - | called from TIM2 ISR when countdown elapsed |
| 0x080175C0 | 0x0801762C | 108 | B | DAC_Init_PA4 | medium | 7 | 1 | - | clk PA/DAC, PA4 analog, DAC ch1 init/enable, data=0, PA4 set bit |
| 0x0801761E | 0x08017626 | 8 | B | sub_0801761E | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801762C | 0x080176CE | 162 | B | NAND_GPIO_FSMC_Init | high | 5 | 1 | - | PD pins 0xD8B3 AF_PP, PE 0x780 AF_PP, PD6 IPU (NWAIT), PE0 IPU, FSMC_NANDInit, enable |
| 0x080176CE | 0x080176F4 | 38 | B | NAND_ReadID | high | 0 | 1 | FSMC_BANK2(NAND) | CMD 0x90, ADDR 0x00, read 2x DATA |
| 0x080176F4 | 0x0801772A | 54 | B | sub_080176F4 | auto | 0 | 2 | - | unknown |
| 0x0801772A | 0x08017746 | 28 | B | NAND_ReadStatus | high | 0 | 1 | FSMC_BANK2(NAND) | CMD 0x70, read DATA |
| 0x08017746 | 0x0801776C | 38 | B | sub_08017746 | auto | 1 | 2 | - | unknown |
| 0x0801776C | 0x08017810 | 164 | B | NAND_WriteAddr | medium | 3 | 4 | FSMC_BANK2(NAND) | writes 5 address cycles (col lo/hi, row x3) |
| 0x08017810 | 0x0801789A | 138 | B | NAND_ReadPage | high | 3 | 5 | FSMC_BANK2(NAND) | CMD 0x00, 5 ADDR, CMD 0x30, read DATA |
| 0x080179C0 | 0x080179F8 | 56 | B | NAND_EraseBlock | high | 1 | 2 | FSMC_BANK2(NAND) | CMD 0x60, 3 ADDR, CMD 0xD0 |
| 0x080179F8 | 0x08017A02 | 10 | B | NAND_Reset | high | 0 | 0 | FSMC_BANK2(NAND) | CMD 0xFF |
| 0x08017A02 | 0x08017A82 | 128 | B | sub_08017A02 | auto | 2 | 1 | - | auto: strings: '%d/%d' |
| 0x08017A82 | 0x08017BCA | 328 | B | NAND_Erase_Progress | medium | 8 | 1 | - | prints "Erasing: %d/%d", "error block:", "error num: %d" |
| 0x08017BCA | 0x08017BDE | 20 | B | sub_08017BCA | auto | 0 | 1 | - | unknown |
| 0x08017BDE | 0x08017C28 | 74 | B | NAND_ReadPageAt | low | 0 | 8 | - | page/row computation wrapper used by image loader |
| 0x08017C28 | 0x08017CBE | 150 | B | sub_08017C28 | auto | 2 | 4 | - | unknown |
| 0x08017CBE | 0x08017DA4 | 230 | B | sub_08017CBE | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08017DA4 | 0x08017DCE | 42 | B | sub_08017DA4 | auto | 0 | 1 | - | unknown |
| 0x08017DCE | 0x08017E7C | 174 | B | SPI3_DMA_Init_unused | medium | 4 | 0 | RCC,AFIO,SPI3 | AFIO remap, PB3/PB5/PC7/PA15 AF, SPI3_Init; no static callers |
| 0x08017E7C | 0x08017EE0 | 100 | B | sub_08017E7C | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08017F08 | 0x08017F20 | 24 | B | sub_08017F08 | auto | 0 | 4 | DMA2,SPI3 | auto: touches DMA2, SPI3 |
| 0x08017F20 | 0x08017F54 | 52 | B | sub_08017F20 | auto | 1 | 2 | - | unknown |
| 0x08017F54 | 0x08017FC4 | 112 | B | DMA2_Ch2_IRQHandler | medium | 2 | 0 | DMA2 | DMA2 ISR/IFCR handling for SPI3 path |
| 0x08017FC4 | 0x08017FF0 | 44 | B | sub_08017FC4 | auto | 0 | 0 | DMA2,SPI3 | auto: touches DMA2, SPI3 / no static callers (dead code or called via pointer) |
| 0x08017FF0 | 0x0801800A | 26 | B | sub_08017FF0 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801800A | 0x08018072 | 104 | B | sub_0801800A | auto | 2 | 0 | DMA2 | auto: touches DMA2 / no static callers (dead code or called via pointer) |
| 0x08018074 | 0x0801810C | 152 | B | sub_08018074 | auto | 1 | 0 | DMA2,SPI3 | auto: touches DMA2, SPI3 / no static callers (dead code or called via pointer) |
| 0x080180CC | 0x080180F0 | 36 | B | sub_080180CC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080180D8 | 0x0801811C | 68 | B | sub_080180D8 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801811C | 0x08018122 | 6 | B | sub_0801811C | auto | 0 | 2 | - | unknown |
| 0x08018122 | 0x08018128 | 6 | B | sub_08018122 | auto | 0 | 29 | - | unknown |
| 0x08018128 | 0x08018260 | 312 | B | sub_08018128 | auto | 3 | 1 | - | unknown |
| 0x08018260 | 0x0801842E | 462 | B | sub_08018260 | auto | 13 | 0 | - | auto: strings: 'A0\nA1\nA2\nA3\nA20\nA4\r\n'; '%.0f  '; '%.0f  ' / no static callers (dead code or called via  |
| 0x0801842E | 0x08018430 | 2 | B | sub_0801842E | auto | 0 | 5 | - | unknown |
| 0x08018430 | 0x080184C0 | 144 | B | sub_08018430 | auto | 4 | 2 | - | unknown |
| 0x08018480 | 0x080184FC | 124 | B | sub_08018480 | auto | 3 | 1 | - | unknown |
| 0x08018518 | 0x0801851E | 6 | B | sub_08018518 | auto | 0 | 4 | - | unknown |
| 0x0801851E | 0x08018536 | 24 | B | sub_0801851E | auto | 0 | 6 | - | unknown |
| 0x08018538 | 0x08018556 | 30 | B | sub_08018538 | auto | 1 | 23 | - | unknown |
| 0x08018556 | 0x080186B4 | 350 | B | sub_08018556 | auto | 3 | 6 | - | unknown |
| 0x080186B8 | 0x080186CE | 22 | B | sub_080186B8 | auto | 0 | 1 | - | unknown |
| 0x080186CE | 0x080186EE | 32 | B | sub_080186CE | auto | 0 | 4 | - | unknown |
| 0x080186EE | 0x0801873E | 80 | B | sub_080186EE | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801873E | 0x08018790 | 82 | B | sub_0801873E | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08018790 | 0x080187B8 | 40 | B | sub_08018790 | auto | 0 | 3 | - | auto: strings: 'A35\n' |
| 0x080187B8 | 0x08018836 | 126 | B | sub_080187B8 | auto | 2 | 1 | - | unknown |
| 0x08018836 | 0x080188A6 | 112 | B | sub_08018836 | auto | 0 | 2 | - | unknown |
| 0x080188A6 | 0x080188F8 | 82 | B | sub_080188A6 | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080188F8 | 0x08018CE4 | 1004 | B | sub_080188F8 | auto | 11 | 0 | - | auto: strings: 'A13 %s\n'; '.bmp'; 'A8 S%d\n' / no static callers (dead code or called via pointer) |
| 0x08018CAE | 0x08018D18 | 106 | B | sub_08018CAE | auto | 4 | 0 | - | auto: strings: 'A8 S0\n' / no static callers (dead code or called via pointer) |
| 0x08018D20 | 0x08018D4A | 42 | B | sub_08018D20 | auto | 0 | 6 | - | unknown |
| 0x08018D4A | 0x08018DF0 | 166 | B | sub_08018D4A | auto | 6 | 0 | - | auto: strings: 'A51 K\r\n'; 'A51 J\r\n'; 'A51 I\r\n' / no static callers (dead code or called via pointer) |
| 0x08018DF0 | 0x08018E10 | 32 | B | sub_08018DF0 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08018E10 | 0x08018F54 | 324 | B | sub_08018E10 | auto | 10 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08019086 | 0x080192CE | 584 | B | sub_08019086 | auto | 12 | 0 | - | auto: strings: 'bmp'; 'BMP'; 'No laser operation allowed' / no static callers (dead code or called via pointer |
| 0x080192CE | 0x0801936A | 156 | B | sub_080192CE | auto | 4 | 1 | - | auto: strings: '%.1f' |
| 0x0801936A | 0x080194B2 | 328 | B | sub_0801936A | auto | 6 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x080194B2 | 0x08019A40 | 1422 | B | sub_080194B2 | auto | 18 | 0 | - | auto: strings: 'A38 S%d\r\n'; 'A40 S%.2f\r\n'; 'A42 S%d\r\n' / no static callers (dead code or called via poin |
| 0x08019AA4 | 0x08019AB0 | 12 | B | sub_08019AA4 | auto | 0 | 8 | - | unknown |
| 0x08019AB0 | 0x08019AD0 | 32 | B | sub_08019AB0 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08019AD0 | 0x08019B30 | 96 | B | sub_08019AD0 | auto | 6 | 0 | - | auto: strings: 'A16 C230\n'; 'A16 C230\n' / no static callers (dead code or called via pointer) |
| 0x08019B30 | 0x08019B52 | 34 | B | sub_08019B30 | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08019B52 | 0x08019CFC | 426 | B | sub_08019B52 | auto | 13 | 0 | - | auto: strings: 'A0\nA1\n'; '  %.0f/%.0f  '; 'A22 E -30 F400\n' / no static callers (dead code or called via po |
| 0x08019CFC | 0x08019D1E | 34 | B | sub_08019CFC | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x08019D1E | 0x0801A068 | 842 | B | sub_08019D1E | auto | 14 | 0 | - | auto: strings: 'A0\nA1\nA2\nA3\n'; '  %.0f/%.0f  '; '  %.0f/%.0f  ' / no static callers (dead code or called v |
| 0x0801A104 | 0x0801A634 | 1328 | B | sub_0801A104 | auto | 8 | 0 | - | auto: strings: 'A22 X-0.1 F%d\n'; 'A22 X-1.0 F%d\n'; 'A22 X-10.0 F%d\n' / no static callers (dead code or call |
| 0x0801A634 | 0x0801A680 | 76 | B | sub_0801A634 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801A720 | 0x0801A8E0 | 448 | B | sub_0801A720 | auto | 12 | 0 | - | auto: strings: 'A25\n'; 'Printer is running Please try '; 'Done !' / no static callers (dead code or called vi |
| 0x0801A8E0 | 0x0801A9C0 | 224 | B | sub_0801A8E0 | auto | 10 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801AA70 | 0x0801AB10 | 160 | B | sub_0801AA70 | auto | 2 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801AB10 | 0x0801AB84 | 116 | B | sub_0801AB10 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801AB84 | 0x0801AD34 | 432 | B | sub_0801AB84 | auto | 6 | 6 | - | auto: strings: 'YES' |
| 0x0801AD34 | 0x0801AD66 | 50 | B | sub_0801AD34 | auto | 4 | 1 | - | unknown |
| 0x0801AD66 | 0x0801B11E | 952 | B | Main_Task_UI | medium | 9 | 1 | - | big UI/state task called each loop iteration; strings "T0 senser abnormal", ... |
| 0x0801B1D0 | 0x0801B288 | 184 | B | sub_0801B1D0 | auto | 8 | 0 | - | auto: strings: 'A11\r\n'; 'A11\r\n' / no static callers (dead code or called via pointer) |
| 0x0801B288 | 0x0801B348 | 192 | B | sub_0801B288 | auto | 6 | 0 | - | auto: strings: 'A9\r\n'; 'pause failed' / no static callers (dead code or called via pointer) |
| 0x0801B348 | 0x0801BA18 | 1744 | B | sub_0801B348 | auto | 28 | 0 | - | auto: strings: 'A5\nA6\nA7\nA20\n'; ' %02d:%02d '; '%d  ' / no static callers (dead code or called via pointer |
| 0x0801BA18 | 0x0801BA5A | 66 | B | sub_0801BA18 | auto | 4 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801BA5A | 0x0801BC08 | 430 | B | sub_0801BA5A | auto | 5 | 1 | - | auto: strings: 'No Files' |
| 0x0801BC08 | 0x0801BD52 | 330 | B | sub_0801BC08 | auto | 10 | 0 | - | auto: strings: ' Are you sure to delete it?' / no static callers (dead code or called via pointer) |
| 0x0801BD52 | 0x0801BDAC | 90 | B | sub_0801BD52 | auto | 5 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801BE08 | 0x0801C33E | 1334 | B | sub_0801BE08 | auto | 17 | 0 | - | auto: strings: 'bmp'; 'Picture pixels cannot  \nexceed'; 'Picture pixels cannot  \nexceed' / no static callers |
| 0x0801C33E | 0x0801C374 | 54 | B | sub_0801C33E | auto | 3 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801C3E0 | 0x0801C3FC | 28 | B | sub_0801C3E0 | auto | 0 | 1 | - | unknown |
| 0x0801C3FC | 0x0801C8D0 | 1236 | B | Main_Task_Comm_Parse | medium | 13 | 1 | - | big task called each loop iteration; consumes uart_get_line; references protocol strings |
| 0x0801C8D2 | 0x0801C95C | 138 | B | sub_0801C8D2 | auto | 5 | 0 | - | auto: strings: 'A0\nA1\nA2\nA3\n'; '  %.0f/%.0f  '; '  %.0f/%.0f  ' / no static callers (dead code or called v |
| 0x0801C95C | 0x0801CA6C | 272 | B | sub_0801C95C | auto | 8 | 1 | - | auto: strings: 'A0\nA2\n'; ' %.0f '; '%.0f ' |
| 0x0801CA6C | 0x0801CAC2 | 86 | B | sub_0801CA6C | auto | 4 | 1 | - | auto: strings: ' %.0f ' |
| 0x0801CAC2 | 0x0801CB18 | 86 | B | sub_0801CAC2 | auto | 4 | 1 | - | auto: strings: ' %.0f ' |
| 0x0801CB18 | 0x0801CB46 | 46 | B | sub_0801CB18 | auto | 2 | 1 | - | auto: strings: 'A16 S%.0f \r\n'; 'A17 S%.0f \r\n'; 'A1\r\nA3\r\n' |
| 0x0801CB46 | 0x0801CB50 | 10 | B | sub_0801CB46 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801CC90 | 0x0801CD74 | 228 | B | sub_0801CC90 | auto | 2 | 0 | - | auto: strings: ' %d%% ' / no static callers (dead code or called via pointer) |
| 0x0801CD76 | 0x0801CDBC | 70 | B | sub_0801CD76 | auto | 2 | 0 | - | auto: strings: ' %d%% ' / no static callers (dead code or called via pointer) |
| 0x0801CDBC | 0x0801CDDC | 32 | B | sub_0801CDBC | auto | 1 | 0 | - | auto: strings: 'A18 S%d \r\n'; 'A20 S%d \r\n'; 'A20\r\nA4\r\n' / no static callers (dead code or called via po |
| 0x0801CDDC | 0x0801CDE6 | 10 | B | sub_0801CDDC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801CDE6 | 0x0801CE0C | 38 | B | sub_0801CDE6 | auto | 0 | 7 | - | unknown |
| 0x0801CE0C | 0x0801CECC | 192 | B | sub_0801CE0C | auto | 2 | 4 | - | auto: strings: '[%d]=%d   ' |
| 0x0801CEA2 | 0x0801CECC | 42 | B | sub_0801CEA2 | auto | 1 | 0 | - | auto: strings: '[%d]=%d   ' / no static callers (dead code or called via pointer) |
| 0x0801CF40 | 0x0801CF56 | 22 | B | Param_ReadFlash | high | 0 | 2 | - | word copy from 0x0803E864+r0 into r1, r2 words |
| 0x0801CF56 | 0x0801CFB0 | 90 | B | sub_0801CF56 | auto | 5 | 1 | - | unknown |
| 0x0801CFB0 | 0x0801CFD4 | 36 | B | B_Reset_Handler | high | 0 | 0 | - | blx SystemInit(0x0801D074), then bx 0x08010131 (scatter-load wrapper) |
| 0x0801CFCA | 0x0801CFCC | 2 | B | sub_0801CFCA | auto | 0 | 0 | - | unknown |
| 0x0801CFD4 | 0x0801D074 | 160 | B | SetSysClock_HSE_PLLx15 | high | 0 | 1 | RCC,FLASH_IF | HSE on, flash ACR=prefetch+2WS, PPRE1=/2, PLL=HSE*15, switch SYSCLK to PLL |
| 0x0801D074 | 0x0801D0B4 | 64 | B | SystemInit | high | 1 | 1 | RCC,SCB | RCC reset to default, calls SetSysClock (0x0801CFD4), VTOR=0x08000000 |
| 0x0801D0B6 | 0x0801D12C | 118 | B | sub_0801D0B6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801D12C | 0x0801D144 | 24 | B | sub_0801D12C | auto | 0 | 5 | - | unknown |
| 0x0801D144 | 0x0801D168 | 36 | B | sub_0801D144 | auto | 0 | 6 | - | unknown |
| 0x0801D168 | 0x0801D176 | 14 | B | sub_0801D168 | auto | 0 | 21 | - | unknown |
| 0x0801D176 | 0x0801D188 | 18 | B | sub_0801D176 | auto | 0 | 2 | - | unknown |
| 0x0801D188 | 0x0801D1A2 | 26 | B | sub_0801D188 | auto | 2 | 2 | - | unknown |
| 0x0801D1A2 | 0x0801D71E | 1404 | B | sub_0801D1A2 | auto | 0 | 5 | - | unknown |
| 0x0801D246 | 0x0801D24C | 6 | B | sub_0801D246 | auto | 0 | 3 | - | unknown |
| 0x0801D24C | 0x0801D252 | 6 | B | sub_0801D24C | auto | 0 | 1 | - | unknown |
| 0x0801D252 | 0x0801D2B6 | 100 | B | sub_0801D252 | auto | 0 | 3 | - | unknown |
| 0x0801D2B6 | 0x0801D6C2 | 1036 | B | sub_0801D2B6 | auto | 0 | 3 | - | unknown |
| 0x0801D332 | 0x0801D34A | 24 | B | sub_0801D332 | auto | 0 | 1 | - | unknown |
| 0x0801D34A | 0x0801D71E | 980 | B | sub_0801D34A | auto | 0 | 6 | - | unknown |
| 0x0801D35C | 0x0801D71E | 962 | B | sub_0801D35C | auto | 0 | 3 | - | unknown |
| 0x0801D366 | 0x0801D380 | 26 | B | sub_0801D366 | auto | 1 | 1 | - | unknown |
| 0x0801D380 | 0x0801D3B2 | 50 | B | sub_0801D380 | auto | 0 | 4 | - | unknown |
| 0x0801D3B2 | 0x0801D3DA | 40 | B | sub_0801D3B2 | auto | 0 | 4 | - | unknown |
| 0x0801D3DA | 0x0801D40C | 50 | B | sub_0801D3DA | auto | 1 | 1 | - | unknown |
| 0x0801D3DE | 0x0801D40C | 46 | B | sub_0801D3DE | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801D40C | 0x0801D432 | 38 | B | sub_0801D40C | auto | 0 | 13 | - | unknown |
| 0x0801D434 | 0x0801D464 | 48 | B | sub_0801D434 | auto | 0 | 1 | - | unknown |
| 0x0801D464 | 0x0801D494 | 48 | B | sub_0801D464 | auto | 0 | 2 | - | unknown |
| 0x0801D494 | 0x0801D6C2 | 558 | B | sub_0801D494 | auto | 0 | 3 | - | unknown |
| 0x0801D4CC | 0x0801D4E0 | 20 | B | sub_0801D4CC | auto | 0 | 4 | - | unknown |
| 0x0801D4E0 | 0x0801D4F4 | 20 | B | sub_0801D4E0 | auto | 0 | 3 | - | unknown |
| 0x0801D4F4 | 0x0801D520 | 44 | B | sub_0801D4F4 | auto | 0 | 1 | - | unknown |
| 0x0801D520 | 0x0801D582 | 98 | B | sub_0801D520 | auto | 2 | 2 | - | unknown |
| 0x0801D582 | 0x0801D5A2 | 32 | B | sub_0801D582 | auto | 0 | 5 | - | unknown |
| 0x0801D5A4 | 0x0801D5DA | 54 | B | sub_0801D5A4 | auto | 1 | 1 | - | unknown |
| 0x0801D5DA | 0x0801D632 | 88 | B | sub_0801D5DA | auto | 1 | 1 | - | unknown |
| 0x0801D640 | 0x0801D6B0 | 112 | B | sub_0801D640 | auto | 3 | 1 | - | unknown |
| 0x0801D73C | 0x0801D7D8 | 156 | B | sub_0801D73C | auto | 2 | 4 | - | unknown |
| 0x0801D7D8 | 0x0801D91A | 322 | B | sub_0801D7D8 | auto | 3 | 1 | - | unknown |
| 0x0801D926 | 0x0801DA0A | 228 | B | sub_0801D926 | auto | 1 | 2 | - | unknown |
| 0x0801DA0A | 0x0801DAE8 | 222 | B | sub_0801DA0A | auto | 0 | 2 | - | unknown |
| 0x0801DAE8 | 0x0801DB8A | 162 | B | sub_0801DAE8 | auto | 1 | 1 | - | unknown |
| 0x0801DAF6 | 0x0801DAFE | 8 | B | sub_0801DAF6 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801DB8A | 0x0801DBBA | 48 | B | sub_0801DB8A | auto | 0 | 1 | - | unknown |
| 0x0801DBBC | 0x0801DBFE | 66 | B | B_scatterload | high | 1 | 1 | - | walks table 0x08023308..0x08023328 (src,dst,size,handler) and calls each handler |
| 0x0801DBE0 | 0x0801DBFE | 30 | B | sub_0801DBE0 | auto | 0 | 3 | - | unknown |
| 0x0801DBFE | 0x0801DC22 | 36 | B | sub_0801DBFE | auto | 0 | 1 | - | unknown |
| 0x0801DC24 | 0x0801DC2C | 8 | B | sub_0801DC24 | auto | 0 | 2 | - | unknown |
| 0x0801DC2C | 0x0801DC3E | 18 | B | sub_0801DC2C | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801DC40 | 0x0801DD40 | 256 | B | sub_0801DC40 | auto | 3 | 1 | - | unknown |
| 0x0801DD40 | 0x0801DF78 | 568 | B | sub_0801DD40 | auto | 3 | 1 | - | unknown |
| 0x0801DF78 | 0x0801DF96 | 30 | B | sub_0801DF78 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801DF96 | 0x0801DFB8 | 34 | B | sub_0801DF96 | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801DFB8 | 0x0801E056 | 158 | B | sub_0801DFB8 | auto | 2 | 1 | - | unknown |
| 0x0801E056 | 0x0801E072 | 28 | B | sub_0801E056 | auto | 0 | 1 | - | unknown |
| 0x0801E072 | 0x0801E08A | 24 | B | sub_0801E072 | auto | 1 | 1 | - | unknown |
| 0x0801E08A | 0x0801E0E0 | 86 | B | B_scatter_copy | medium | 0 | 0 | - | RW data copy handler (table entry 0) |
| 0x0801E0E0 | 0x0801E100 | 32 | B | sub_0801E0E0 | auto | 1 | 22 | - | unknown |
| 0x0801E100 | 0x0801E128 | 40 | B | sub_0801E100 | auto | 2 | 19 | - | unknown |
| 0x0801E128 | 0x0801E130 | 8 | B | sub_0801E128 | auto | 0 | 3 | - | unknown |
| 0x0801E130 | 0x0801E13C | 12 | B | sub_0801E130 | auto | 0 | 1 | - | unknown |
| 0x0801E13C | 0x0801E14A | 14 | B | sub_0801E13C | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801E14C | 0x0801E15A | 14 | B | B_scatter_zeroinit | medium | 0 | 0 | - | ZI clear handler (table entry 1) |
| 0x0801E15C | 0x0801E168 | 12 | B | sub_0801E15C | auto | 0 | 3 | - | unknown |
| 0x0801E168 | 0x0801E2CC | 356 | B | sub_0801E168 | auto | 6 | 1 | - | unknown |
| 0x0801E2CC | 0x0801E2DA | 14 | B | sub_0801E2CC | auto | 0 | 1 | - | unknown |
| 0x0801E2DC | 0x0801E9AC | 1744 | B | sub_0801E2DC | auto | 5 | 2 | - | auto: strings: '0123456789abcdef'; '0123456789ABCDEF' |
| 0x0801E9B8 | 0x0801E9DC | 36 | B | sub_0801E9B8 | auto | 0 | 1 | - | unknown |
| 0x0801E9CC | 0x0801E9DC | 16 | B | sub_0801E9CC | auto | 0 | 0 | - | auto: no static callers (dead code or called via pointer) |
| 0x0801E9DC | 0x0801EA0A | 46 | B | sub_0801E9DC | auto | 0 | 1 | - | unknown |
| 0x0801EA0A | 0x0801EA14 | 10 | B | sub_0801EA0A | auto | 0 | 1 | - | unknown |
| 0x0801EA14 | 0x0801EA3E | 42 | B | sub_0801EA14 | auto | 3 | 2 | - | unknown |
| 0x0801EA3E | 0x0801EA8A | 76 | B | sub_0801EA3E | auto | 2 | 1 | - | unknown |
| 0x0801EA5E | 0x0801EA8A | 44 | B | sub_0801EA5E | auto | 1 | 0 | - | auto: no static callers (dead code or called via pointer) |
