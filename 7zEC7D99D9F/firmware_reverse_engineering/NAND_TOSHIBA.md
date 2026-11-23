# NAND_TOSHIBA — TC58BVG0S3H (образ B: 0x080176CE…; образ A: копия 0x08008B0A…)

## Шина и GPIO
* NAND Bank2: DATA=0x70000000, CMD=0x70010000, ADDR=0x70020000 (ссылки в mem-логе: `FSMC_BANK2`). `FSMC_NANDInit` вызывается один раз (0x080176BE). Включение `FSMC_NANDCmd`; RCC AHB (0x080114D0 вызывается из 0x0801762C).
* Конфиг `FSMC_NAND_InitTypeDef` (стек, вызов 0x080176BE; раскладка SPL подтверждена чтением `FSMC_NANDInit` 0x08010D1A–0x08010D64): Bank=**0x10** (FSMC_Bank2_NAND), MemoryDataWidth=**0** (8 бит), **ECCPageSize=0x00060000 = FSMC_ECCPageSize_2048Bytes**, Waitfeature и ECC-enable — не константы (UNRESOLVED), тайминги: **SetupTime=1, HoldSetupTime=2** (WaitSetupTime/HiZSetupTime — не константы). Запись в регистры: PCR2 (+0x60), PMEM2 (+0x68), PATT2 (+0x6C) (0x08010D78–0x08010D7C).
* Пины: PD0,1,4,5,7(NCE2),11(CLE),12(ALE),14,15 AF_PP; PE7–10 AF_PP; PD6 IPU (NWAIT/RB); PE0 IPU.

## Команды (подтверждены записями в 0x70010000)
| Операция | Функция B / A | Последовательность |
|---|---|---|
| Reset | 0x080179F8 / 0x08008F58 | CMD FF |
| Read ID | 0x080176CE / 0x08008B0A | CMD 90, ADDR 00, чтение 2×DATA (остальные ID-байты не читаются) |
| Read status | 0x0801772A / 0x08008B6E | CMD 70, чтение DATA |
| Read page | 0x08017810 / 0x08008C8A (main) / 0x08008E14 (spare) | CMD 00, ADDR×5 (col lo, col hi, row×3), CMD 30, чтение DATA; **col=0x0800 для spare** (A: 0x08008E14) |
| Program page | A: 0x08008BC0 (main) / 0x08008D48 (spare); B: через 0x0801776C | CMD 80, ADDR×5, DATA, CMD 10 |
| Erase block | 0x080179C0 / 0x08008EEA | CMD 60, ADDR×3 (row), CMD D0 |

## Геометрия (выведено)
* 5 адресных циклов чтения (2 колонка + 3 строка), колонка 0x0800 для spare и ECCPageSize=2048 ⇒ **страница 2048 B + spare (64 B)**, как у TC58BVG0S3H (по даташиту блок = 64 стр. = 128 КБ — внешний факт; в коде размер блока не константа).
* ECC/коррекция, bad-block-таблица: **не найдены** в B (нет чтений spare в B). В A есть чтение/запись spare (0x08008D48/0x08008E14) — вероятная работа с маркерами (**не проанализировано**). B при «Erasing» печатает `error block:` / `error num: %d` (0x08017D63, 0x08017D88; функция 0x08017A82) — есть учёт ошибок стирания.

## Формат хранения (доказано `Show_NAND_Image` 0x080148EA)
* Изображение №n лежит в NAND со смещения **n × 3 × 0x20000** (0x080148EE `add r0,r0,r0,lsl#1`, 0x080148F2 `lsls #17`) = 3 блока (384 КБ) на картинку.
* Читается **150 страниц по 0x800 B** (0x08014940 `cmp r4,#0x96`, шаг 0x800 в 0x08014932), каждая выводится как **0x400 пикселей** (0x08014912 `mov.w r7,#0x400`) в окно `(0,0)-(0x1DF,0x13F)` ⇒ 150×1024 = 153 600 = 480×320 пикселей RGB565 (307 200 B).
* После загрузки с SD `B_main` показывает картинки 0x41…0x70 (48 шт., `add r0,r4,#0x41`, `cmp r4,#0x30`, пауза 200 тиков, 0x0801019E–0x080101B0). На каждом запуске далее вызывается `Show_All_Images_Test` (0x080101C4).
* Номера: 0…0x3C (61 шт.) в тестовом `Show_All_Images_Test` 0x08014946; задержка 3000 после (0x0801495C).
* Загрузка ресурсов с SD на NAND: `B_main` вызывает `SD_Init` → при успехе `0x08014250`, и при условии «значение в RAM > 6» (сравнение `cmp r0,#6` в `B_main`, см. `full_disassembly.asm` 0x08010144–0x080101CC) → `NAND_Erase_Progress` 0x08017A82 («Erasing: %d/%d») → `SD_to_NAND_Loader` 0x08014702 («Loading...: %d/%d»). Имена/формат файлов на SD не найдены как ASCII (см. UNRESOLVED).
* NAND хранит **графику UI (полноэкранные картинки)**; шрифты в NAND не обнаружены — шрифтовые/кодовые таблицы лежат во Flash МК.
