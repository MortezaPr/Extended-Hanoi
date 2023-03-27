# Extended Hanoi

The Tower of Hanoi is a mathematical puzzle that consists of three rods and a variable number of disks of different sizes, which can slide onto any rod.
The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

In my extended version of the Tower of Hanoi, the puzzle starts with the disks in a neat stack in ascending order of size on all three rods.
The objective is to move all the disks to one rod, obeying the same rules as the classic Tower of Hanoi puzzle.

## Getting Started

To run the game, clone this repository and run 'exHanoiGUI.py'.

``` 
git clone https://github.com/MortezaPr/ExHanoi.git
cd ExHanoi
python exHanoi_GUI.py
```

## Usage

Once you've launched the program, you'll be presented with a graphical user interface where you can configure the number of disks and delay.
After setting the parameters, click the "Start" button to begin the puzzle. The program will display the moves taken to solve the puzzle.

## Controls

In manual mode, you can move through the steps using the "Next" button. You can pause and resume the game using the respective buttons.
In both modes, you can reset the game using the "Reset" button, and you can end the game with the "Final" button.

## Built With

* Python 3
* tkinter library

