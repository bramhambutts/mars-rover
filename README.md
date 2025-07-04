# Mars Rover

The aim of this program is to simulate the movement of Mars rovers in a similar style to turtle programs. It will take in small inputs for creating the plateau the rovers will act on, placing rovers, and moving the rovers.

## How to move around

To create the plateau, enter 2 numbers representing the x and y coordinate size of the grid. A rover can then be created at a given position and direction. Movement can then be dictated through the letters `L`, `R`, and `M`, meaning left, right, and move respectively. Movement is only one grid space at a time.

An example to move the rover diagonally by two squares would be:
- `5 5`
- `0 0 N`
- `MLMRMLM`

## Importing the project

All libraries are included in the `requirements.txt` file, and can be installed via `pip install -r requirements.txt`. The program can then be run by `python main.py`.

## How it works

The plateau and rovers are all managed by `MissionControl`. The `InputParser` manages how input is handled, and will output appropriate objects depending on the input, being either `PlateauSize`, `RoverPosition`, or a list of `Instructions`.