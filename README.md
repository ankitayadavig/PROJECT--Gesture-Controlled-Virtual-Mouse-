# Gesture-Controlled Virtual Mouse

This project lets you control parts of a Windows desktop using hand gestures captured from a webcam. It also includes an optional assistant called `Proton` that provides a small desktop chat UI plus voice or text commands for launching gesture control and basic desktop actions.

## What It Does

- Tracks hand landmarks with MediaPipe
- Moves the mouse pointer with hand motion
- Supports left click, right click, and double click gestures
- Supports drag and drop
- Supports vertical and horizontal scrolling
- Supports system volume and screen brightness control
- Includes `Proton`, a Windows assistant with a lightweight Eel UI

## Project Structure

```text
src/
  Gesture_Controller.py
  Gesture_Controller_Gloved.py
  Proton.py
  app.py
  web/
```

## Requirements

- Windows
- Python `3.8.x`
- Webcam

This repo is currently set up around Python 3.8 on Windows. Some dependencies, especially `mediapipe`, are sensitive to Python version.

## Installation

1. Create and activate a virtual environment with Python 3.8.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

If microphone input is needed for voice commands, make sure your system has a working microphone setup and install any missing audio dependencies required by `SpeechRecognition` on Windows.

## Run

### Option 1: Gesture controller only

From the project root:

```bash
python src/Gesture_Controller.py
```

This opens the webcam feed and starts gesture recognition directly.

### Option 2: Proton assistant

From the project root:

```bash
python src/Proton.py
```

This starts:

- the Proton assistant
- a small Eel desktop UI
- text input support through the UI
- optional voice-command handling if microphone support is available

If Chrome does not launch for the Eel window, the app falls back to the default browser automatically.

## Core Gestures

The exact recognition logic is implemented in [src/Gesture_Controller.py](/d:/PROJECT--Gesture-Controlled-Virtual-Mouse-/src/Gesture_Controller.py:1).

- Move cursor
- Left click
- Right click
- Double click
- Drag and drop
- Scroll vertically
- Scroll horizontally
- Adjust volume
- Adjust brightness

## Proton Commands

`Proton` supports voice or UI text commands such as:

- `proton launch gesture recognition`
- `proton stop gesture recognition`
- `proton search ...`
- `proton date`
- `proton time`
- `proton copy`
- `proton paste`
- `proton list`
- `proton open <number>`
- `proton back`
- `proton exit`

The main assistant flow lives in [src/Proton.py](/d:/PROJECT--Gesture-Controlled-Virtual-Mouse-/src/Proton.py:1).

## Key Dependencies

- `opencv-contrib-python`
- `mediapipe`
- `pyautogui`
- `pycaw`
- `screen-brightness-control`
- `SpeechRecognition`
- `pyttsx3`
- `eel`

See [requirements.txt](/d:/PROJECT--Gesture-Controlled-Virtual-Mouse-/requirements.txt:1) for the pinned versions used in this repo.

## Notes

- The project is designed primarily for Windows desktop control.
- `Gesture_Controller.py` includes a helpful error if `mediapipe` is missing or the wrong Python version is being used.
- `Proton` can continue in text-only mode if microphone or text-to-speech initialization fails.

## Future Improvements

- Add screenshots or GIF demos stored directly in this repo
- Document the gesture mappings more explicitly
- Add troubleshooting for camera, microphone, and browser issues
- Add a proper architecture overview in `ML_System_Architecture.md`
