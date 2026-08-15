# Heart Drawing with Python Turtle Graphics

## Project Overview

This project uses Python's `turtle` graphics library to draw an animated heart shape. The program creates a beautiful heart design with a white outline and blue fill on a black background.

## What the Code Does

The `heart.py` script performs the following:

1. **Initializes Turtle Graphics**: Sets up a graphics window with a black background
2. **Configures Turtle Settings**: 
   - Sets drawing speed to 3
   - Sets pen size to 3
   - Sets colors to white (outline) and blue (fill)
3. **Draws the Heart**: Uses a custom `draw()` function to create smooth curves that form the heart shape
4. **Animation**: The turtle moves at a moderate speed to create a smooth drawing animation

## Requirements

- Python 3.6 or higher
- `tkinter` module (required for turtle graphics)

## Installation

### Step 1: Ensure Python is Installed
```bash
python3 --version
```

### Step 2: Install tkinter (if not already installed)

**On Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install -y python3-tk
```

**On macOS (with Homebrew):**
```bash
brew install python-tk@3.10
```

**On Windows:**
- `tkinter` is included by default with Python

## How to Run

### Option 1: Run from Terminal (Recommended)
```bash
python3 /home/rab/Desktop/my_projects/Automation/heart.py
```

### Option 2: Run from VS Code
1. Open the `heart.py` file in VS Code
2. Click the **Run** button in the top-right corner of the editor
3. Or press `Ctrl+F5` to run the script

### Option 3: Run from Python Interactive Shell
```bash
python3
>>> exec(open('/home/rab/Desktop/my_projects/Automation/heart.py').read())
```

## Output

When you run the script, a graphics window will open displaying:
- An animated heart shape being drawn
- White outline with blue fill
- Black background
- The animation will complete and the window will remain open until you close it manually

## Code Breakdown

| Component | Description |
|-----------|-------------|
| `turtle.speed(3)` | Sets drawing speed (1=slowest, 10=fastest) |
| `turtle.bgcolor('black')` | Sets background color to black |
| `turtle.pensize(3)` | Sets pen thickness to 3 pixels |
| `draw()` function | Creates curved lines by turning 1° and moving forward 200 times |
| `turtle.begin_fill()` / `turtle.end_fill()` | Fills the heart shape with blue color |
| `turtle.hideturtle()` | Hides the turtle cursor after drawing |
| `turtle.done()` | Keeps the window open until user closes it |

## Troubleshooting

**Error: `ModuleNotFoundError: No module named 'tkinter'`**
- Solution: Install tkinter using the installation steps above

**Window doesn't open**
- Make sure you're not running in a headless environment (without display)
- On remote systems, you may need to set up X11 forwarding

**Drawing is too slow or too fast**
- Change the `turtle.speed()` value (1-10, where 10 is fastest)

## Customization

You can modify the script to change:
- **Colors**: Change `'blue'` and `'blue'` to any valid turtle colors
- **Background**: Change `'white'` to any color
- **Drawing Speed**: Adjust `turtle.speed()` value
- **Pen Size**: Change `turtle.pensize()` value

## Summary

This project demonstrates:
- Basic turtle graphics functionality
- Drawing curves using loops
- Using functions to create reusable code patterns
- Color and styling in graphics programming

Enjoy your animated heart! 