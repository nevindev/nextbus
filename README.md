# NextBus

## Requirements

Nextbus is written in Python 3, and requires a version 3 interpreter.

It requires the [requests](https://requests.readthedocs.io/en/latest/) library for making HTTP requests and [pytest](https://docs.pytest.org/en/7.2.x/) for testing.

A virtual environment called 'venv' has been included with these dependencies already installed via pip.

---

## Getting Started
To start the virtual environment, from the root of the project directory run

    $source /venv/bin/activate

---
## Testing
Due to the import paths of packages in the test directory, navigate to the ``/nextbus`` directory and run

    $python3 -m pytest ../tests

To see how long all the tests take to run, run

    $python3 -m pytest ../tests --durations=0

Pytest will run all the tests for the different modules (and they should all pass!)

---
## Usage
From the root of the project, run

    $python3 nextbus/nextbus.py --route "METRO Blue Line" --stop "Target Field Station Platform 1" --direction south

It should respond with the minutes and seconds until the next departure from the station (if a departure is scheduled). If a departure is not scheduled (the last departure already left) it will print nothing.

    13 minutes 29 seconds

---

## Improper Input
If the route or stop is not recognized, the user will be alerted that a departure cannot be found.
    
    Could not find route Nonexistant Route

<br/>

    
    Could not find stop on route METRO Blue Line matching Nonexistant stop


If an invalid cardinal direction is entered, the program will show the user the valid choices.

    usage: NextBus [-h] -r ROUTE -s STOP -d {south,east,west,north}
    
    NextBus: error: argument -d/--direction: invalid choice: 'northeast' (choose from 'south', 'east', 'west', 'north')