# PyChip8

## Introduction

PyChip8 is the world's first CHIP-8 emulator implemented in Python.

<img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061216_0.PNG" width="200"> <img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_061223_0.PNG" width="200"> <img src="https://github.com/jay-kumogata/PyChip8/blob/master/screenshots/pychip8_070102_0.PNG" width="200">

## How to run

- (a) Install Python3.7 (python-3.7.2.exe), which can be obtained from https://www.python.org/downloads/
- (b) Install the PyGame on Python from the command line:
  - C> python -m pip install pygame
- (c) Unzip the Chip8 game pack (c8games.zip) archive, which can be obtained from http://www.zophar.net/roms.phtml?op=show&type=chip8)
- (d) From the command line, run:
  - C> python PyChip8.py <ROM file name>
  - Example: C> python PyChip8.py c8games/PONG
- (e) Click [x] when finished

## How to control

The keys are mapped as follows.

	Original |1|2|3|C| Mapping to |4|5|6|7|
	         |4|5|6|D|            |R|T|Y|U|
	         |7|8|9|E|            |F|G|H|J|
	         |A|0|B|F|            |V|B|N|M|
           
## Specification
### Memory
- RAM (200H - F10H)
- Hexadecimal font (F10H - F60H)

### Registers
- Data Registers (V0 .. VF)
- Address Registers (I)
- Timers (Delay and Sound)
- Stack (16 word length and stack pointer)

### Graphics
- Sprite (CHIP-8 Mode: 8 x 1 .. 15)
- Collision Flag
- Hexadecimal font
  
### Instruction set
- CHIP-8 instructions (assignment, arithmetic, conditional branch, subroutine call, draw sprite, etc.)

### Keyboard
- Hexadecimal keyboard
