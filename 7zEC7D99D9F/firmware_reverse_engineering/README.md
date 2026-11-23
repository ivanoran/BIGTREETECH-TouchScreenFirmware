# firmware_reverse_engineering

Комплект анализа дампа `original/dump_full.bin` (STM32F10x-класс, Cortex-M3, 256 КБ, база 0x08000000).
SHA-256 дампа: `eb590a761a987de73b56aa42e4dbc61e70cd631e254b94f3dd5ba389951814b3` (размер 262144 Б, оригинал не изменялся).

**Передача другой нейросети/человеку:** начните с `EXECUTIVE_SUMMARY.md` → `MEMORY_MAP.md` → специализированные документы; машинные данные — `disassembly/functions.json`, `references.json`, `cross_references.csv`, `full_disassembly.asm`; неизвестное — `UNRESOLVED.md`.

## Содержимое
Документы: EXECUTIVE_SUMMARY, MEMORY_MAP, VECTOR_TABLE, FUNCTION_INDEX, CALL_GRAPH, PERIPHERALS, CLOCK_TREE, GPIO_MAP, LCD_ILI9488, NAND_TOSHIBA, TOUCH_XPT2046, SD_CARD, UART_PRINTER, TIMERS, SOFTWARE_ARCHITECTURE, STRINGS_AND_RESOURCES, PORTING_GUIDE, UNRESOLVED.
Данные: `disassembly/`, `resources/{strings.txt,binary_regions.csv,extracted_assets/}`, `generated/` (промежуточные таблицы для .md).
Скрипты: `scripts/` (см. scripts/README.md).

## Инструменты и версии
Python 3.12.3 (стандартная библиотека), собственный дизассемблер `scripts/thumb2.py`. Capstone, arm-none-eabi-objdump, Ghidra, radare2 в среде **недоступны** (нет сети) — корректность дизассемблера проверялась на согласованности (отсутствие undefined-опкодов в 1126 трассах, совпадение с независимо известными SPL-паттернами и с вашими предварительными адресами); рекомендуется перекрёстная проверка Ghidra'й: загрузить `original/dump_full.bin`, ARM:LE:32:Cortex, базовый адрес 0x08000000.

## Повтор анализа
```
python3 scripts/run_all.py original/dump_full.bin .
```
## Правила достоверности
Каждый вывод сопровождён адресами инструкций/данных; «гипотеза»/«не подтверждено» — явно; не установленное перечислено в UNRESOLVED.md.
