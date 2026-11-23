# scripts/ — воспроизводимый анализ

Окружение: Python 3 (проверено на `python3 --version` из песочницы — см. корневой README), **только стандартная библиотека** (Pillow использовался лишь для разовых PNG-рендеров шрифтовых гипотез, в пайплайне не нужен). Capstone/objdump/Ghidra/radare2 в среде анализа **отсутствовали** (нет сети), поэтому написан собственный дизассемблер.

| Файл | Назначение |
|---|---|
| `thumb2.py` | дизассемблер ARMv7-M Thumb/Thumb-2 (16-бит + целочисленный 32-бит, IT-блоки, TBB/TBH, MSR/MRS, bit-field, UDIV/SDIV, LDREX/STREX). Не поддерживает FPU/DSP/сопроцессор (в Cortex-M3 их нет) |
| `analyze.py` | обнаружение кода: векторы → рекурсивный спуск → BL-цели → указатели в литералах/данных → скан `push {…,lr}` → скан «дыр»; thunk `ldr rN,=f; bx rN` = tail-call; no-return; фильтр ADR-строк |
| `dataflow.py` | распространение констант по функциям (границы блоков сбрасывают состояние), стек-модель, карта периферии STM32F10x и имена регистров |
| `disassemble.py` | аннотированный листинг (`--func ADDR` печатает одну функцию) |
| `extract_strings.py` | автономный поиск ASCII/UTF-16/GBK-подобных строк |
| `find_references.py ADDR` | функция, xref и обращения к периферии для адреса (после `run_all.py`) |
| `call_sequence.py` | вызовы функции с известными аргументами (так восстановлены GPIO, USART, SPI, TIM структуры) |
| `annotations.py` | ручные имена/описания/evidence (только то, что проверено чтением листинга) |
| `run_all.py` | генерирует все JSON/CSV/ASM, `generated/*.md`, `resources/*`, сырые фрагменты |

## Запуск
```
cd firmware_reverse_engineering
python3 scripts/run_all.py original/dump_full.bin .
python3 scripts/disassemble.py original/dump_full.bin --func 0x0801555A
python3 scripts/call_sequence.py original/dump_full.bin 0x0801738A
python3 scripts/find_references.py 0x08011112
python3 scripts/extract_strings.py original/dump_full.bin --min 6
```
Формат входа: сырой бинарный дамп Flash, **адрес загрузки 0x08000000**, 262144 байт. Время ~10 с.

## Ограничения
* Нет эмуляции: значения регистров известны только если вычисляются из констант внутри базового блока (после метки состояние сбрасывается) — **recall ниже precision**; строки «computed/UNRESOLVED» разрешались вручную.
* Gap-scan может принять за функцию данные, похожие на код; в `functions.json` поле `source` показывает происхождение (`bl`, `vector`, `tail` — надёжно; `prologue`, `gapscan`, `data_ptr`, `lit_ptr` — эвристики).
* `end_address` включает ближайшие литеральные пулы; локальные переменные/аргументы не восстанавливались (`arguments: null`).
* Косвенные вызовы (BLX) не разрешаются автоматически, кроме констант в регистре.

## Проверка результатов
1. SHA-256 дампа (`eb590a761a987de73b56aa42e4dbc61e70cd631e254b94f3dd5ba389951814b3`) = `generated/_stats.json`.
2. Любое утверждение в *.md имеет адрес инструкции: открыть `disassembly/full_disassembly.asm` и найти адрес.
3. Повторный запуск `run_all.py` даёт побайтно идентичные файлы (детерминированно).
