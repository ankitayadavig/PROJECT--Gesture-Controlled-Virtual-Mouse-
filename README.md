# Gesture-Controlled Virtual Mouse

A Windows-based Python project that uses a webcam to control the mouse with hand gestures. It also includes `Proton`, a simple assistant for launching gesture control and basic desktop commands.

## Features

- Move mouse with hand gestures
- Left click, right click, double click
- Drag and drop
- Scroll control
- Volume and brightness control
- Proton assistant with text or voice commands

## Requirements

- Windows
- Python 3.8.x
- Webcam

## Install

```bash
pip install -r requirements.txt
```

## Run

Gesture controller:

```bash
python src/Gesture_Controller.py
```

Proton assistant:

```bash
python src/Proton.py
```

## Files

- `src/Gesture_Controller.py` - main gesture control logic
- `src/Proton.py` - assistant commands
- `src/app.py` - Eel desktop UI

