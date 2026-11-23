
### Vector table at 0x08000000 (image A)

| # | Name | Raw | Handler | Handler name | Note |
|---|---|---|---|---|---|
| 0 | MSP | 0x20007FC8 | -(MSP) | - |  |
| 1 | Reset | 0x080096E9 | 0x080096E8 | A_Reset_Handler |  |
| 2 | NMI | 0x08002E65 | 0x08002E64 | sub_08002E64 |  |
| 3 | HardFault | 0x08002E67 | 0x08002E66 | sub_08002E66 |  |
| 4 | MemManage | 0x08002E6B | 0x08002E6A | sub_08002E6A |  |
| 5 | BusFault | 0x08002E6F | 0x08002E6E | sub_08002E6E |  |
| 6 | UsageFault | 0x08002E73 | 0x08002E72 | sub_08002E72 |  |
| 11 | SVCall | 0x08002E77 | 0x08002E76 | sub_08002E76 |  |
| 12 | DebugMon | 0x08002E79 | 0x08002E78 | sub_08002E78 |  |
| 14 | PendSV | 0x08002E7B | 0x08002E7A | sub_08002E7A |  |
| 15 | SysTick | 0x08002E7D | 0x08002E7C | sub_08002E7C |  |
| 16 | IRQ0_WWDG | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 17 | IRQ1_PVD | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 18 | IRQ2_TAMPER | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 19 | IRQ3_RTC | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 20 | IRQ4_FLASH | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 21 | IRQ5_RCC | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 22 | IRQ6_EXTI0 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 23 | IRQ7_EXTI1 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 24 | IRQ8_EXTI2 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 25 | IRQ9_EXTI3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 26 | IRQ10_EXTI4 | 0x08007FE3 | 0x08007FE2 | sub_08007FE2 |  |
| 27 | IRQ11_DMA1_Ch1 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 28 | IRQ12_DMA1_Ch2 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 29 | IRQ13_DMA1_Ch3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 30 | IRQ14_DMA1_Ch4 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 31 | IRQ15_DMA1_Ch5 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 32 | IRQ16_DMA1_Ch6 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 33 | IRQ17_DMA1_Ch7 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 34 | IRQ18_ADC1_2 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 35 | IRQ19_USB_HP_CAN_TX | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 36 | IRQ20_USB_LP_CAN_RX0 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 37 | IRQ21_CAN_RX1 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 38 | IRQ22_CAN_SCE | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 39 | IRQ23_EXTI9_5 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 40 | IRQ24_TIM1_BRK | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 41 | IRQ25_TIM1_UP | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 42 | IRQ26_TIM1_TRG_COM | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 43 | IRQ27_TIM1_CC | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 44 | IRQ28_TIM2 | 0x08008707 | 0x08008706 | A_TIM2_IRQHandler |  |
| 45 | IRQ29_TIM3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 46 | IRQ30_TIM4 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 47 | IRQ31_I2C1_EV | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 48 | IRQ32_I2C1_ER | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 49 | IRQ33_I2C2_EV | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 50 | IRQ34_I2C2_ER | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 51 | IRQ35_SPI1 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 52 | IRQ36_SPI2 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 53 | IRQ37_USART1 | 0x080088EF | 0x080088EE | A_USART1_IRQHandler |  |
| 54 | IRQ38_USART2 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 55 | IRQ39_USART3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 56 | IRQ40_EXTI15_10 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 57 | IRQ41_RTCAlarm | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 58 | IRQ42_USBWakeup | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 59 | IRQ43_TIM8_BRK | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 60 | IRQ44_TIM8_UP | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 61 | IRQ45_TIM8_TRG_COM | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 62 | IRQ46_TIM8_CC | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 63 | IRQ47_ADC3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 64 | IRQ48_FSMC | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 65 | IRQ49_SDIO | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 66 | IRQ50_TIM5 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 67 | IRQ51_SPI3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 68 | IRQ52_UART4 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 69 | IRQ53_UART5 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 70 | IRQ54_TIM6 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 71 | IRQ55_TIM7 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 72 | IRQ56_DMA2_Ch1 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 73 | IRQ57_DMA2_Ch2 | 0x08009349 | 0x08009348 | sub_08009348 |  |
| 74 | IRQ58_DMA2_Ch3 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |
| 75 | IRQ59_DMA2_Ch4_5 | 0x08009703 | 0x08009702 | sub_08009702 | default/empty handler (infinite loop) |

### Vector table at 0x08010000 (image B)

| # | Name | Raw | Handler | Handler name | Note |
|---|---|---|---|---|---|
| 0 | MSP | 0x20006C08 | -(MSP) | - |  |
| 1 | Reset | 0x0801CFB1 | 0x0801CFB0 | B_Reset_Handler |  |
| 2 | NMI | 0x0801260D | 0x0801260C | sub_0801260C |  |
| 3 | HardFault | 0x0801260F | 0x0801260E | sub_0801260E |  |
| 4 | MemManage | 0x08012611 | 0x08012610 | sub_08012610 |  |
| 5 | BusFault | 0x08012613 | 0x08012612 | sub_08012612 |  |
| 6 | UsageFault | 0x08012615 | 0x08012614 | sub_08012614 |  |
| 11 | SVCall | 0x08012617 | 0x08012616 | sub_08012616 |  |
| 12 | DebugMon | 0x08012619 | 0x08012618 | sub_08012618 |  |
| 14 | PendSV | 0x0801261B | 0x0801261A | sub_0801261A |  |
| 15 | SysTick | 0x0801261D | 0x0801261C | sub_0801261C |  |
| 16 | IRQ0_WWDG | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 17 | IRQ1_PVD | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 18 | IRQ2_TAMPER | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 19 | IRQ3_RTC | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 20 | IRQ4_FLASH | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 21 | IRQ5_RCC | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 22 | IRQ6_EXTI0 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 23 | IRQ7_EXTI1 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 24 | IRQ8_EXTI2 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 25 | IRQ9_EXTI3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 26 | IRQ10_EXTI4 | 0x08016ABB | 0x08016ABA | EXTI4_IRQHandler_vestigial |  |
| 27 | IRQ11_DMA1_Ch1 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 28 | IRQ12_DMA1_Ch2 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 29 | IRQ13_DMA1_Ch3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 30 | IRQ14_DMA1_Ch4 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 31 | IRQ15_DMA1_Ch5 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 32 | IRQ16_DMA1_Ch6 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 33 | IRQ17_DMA1_Ch7 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 34 | IRQ18_ADC1_2 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 35 | IRQ19_USB_HP_CAN_TX | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 36 | IRQ20_USB_LP_CAN_RX0 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 37 | IRQ21_CAN_RX1 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 38 | IRQ22_CAN_SCE | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 39 | IRQ23_EXTI9_5 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 40 | IRQ24_TIM1_BRK | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 41 | IRQ25_TIM1_UP | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 42 | IRQ26_TIM1_TRG_COM | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 43 | IRQ27_TIM1_CC | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 44 | IRQ28_TIM2 | 0x080172C5 | 0x080172C4 | TIM2_IRQHandler |  |
| 45 | IRQ29_TIM3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 46 | IRQ30_TIM4 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 47 | IRQ31_I2C1_EV | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 48 | IRQ32_I2C1_ER | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 49 | IRQ33_I2C2_EV | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 50 | IRQ34_I2C2_ER | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 51 | IRQ35_SPI1 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 52 | IRQ36_SPI2 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 53 | IRQ37_USART1 | 0x08017477 | 0x08017476 | USART1_IRQHandler |  |
| 54 | IRQ38_USART2 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 55 | IRQ39_USART3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 56 | IRQ40_EXTI15_10 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 57 | IRQ41_RTCAlarm | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 58 | IRQ42_USBWakeup | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 59 | IRQ43_TIM8_BRK | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 60 | IRQ44_TIM8_UP | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 61 | IRQ45_TIM8_TRG_COM | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 62 | IRQ46_TIM8_CC | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 63 | IRQ47_ADC3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 64 | IRQ48_FSMC | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 65 | IRQ49_SDIO | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 66 | IRQ50_TIM5 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 67 | IRQ51_SPI3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 68 | IRQ52_UART4 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 69 | IRQ53_UART5 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 70 | IRQ54_TIM6 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 71 | IRQ55_TIM7 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 72 | IRQ56_DMA2_Ch1 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 73 | IRQ57_DMA2_Ch2 | 0x08017F55 | 0x08017F54 | DMA2_Ch2_IRQHandler |  |
| 74 | IRQ58_DMA2_Ch3 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
| 75 | IRQ59_DMA2_Ch4_5 | 0x0801CFCB | 0x0801CFCA | sub_0801CFCA | default/empty handler (infinite loop) |
