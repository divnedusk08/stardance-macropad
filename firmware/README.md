# StarDance firmware

KMK / CircuitPython for Seeed XIAO RP2040.

1. Flash [KMK](https://github.com/KMKfw/kmk_firmware) (or CircuitPython + KMK) onto the XIAO.
2. Copy `main.py` onto the `CIRCUITPY` drive.

Pin map (matches the PCB):

| Switch | GPIO |
|--------|------|
| SW1 | D10 |
| SW2 | D9 |
| SW3 | D8 |

Default keymap: Copy, Paste, Undo. Edit `keyboard.keymap` in `main.py` to change that.
