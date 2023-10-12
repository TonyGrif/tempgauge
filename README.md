# CPU Temperature Analysis

## Requirements
* [Python 3.11](https://www.python.org/)

## Running Instructions
This program can be run with the following command: `./main.py [text file]` in which the text file contains CPU temperature data in the following format with each new line signifying a new reading at a different time:
```
[core1 temp] [core2 temp] ... [coreN temp]
...
[core1 temp] [core2 temp] ... [coreN temp]
```

If this program is run without any arguments, the following usage error message will be outputted: `usage: cpu-temperature [-h] txt_file`

Invalid text file formatting will not be checked for and will result in undefined behavior.

## Sample Execution & Output
When this program is run with `./main.py resources/sensors-with-label.txt`, the first five lines of the output will be as follows:
```
(0, [65.0, 68.0, 54.0, 63.0])
(30, [76.0, 75.0, 65.0, 71.0])
(60, [77.0, 77.0, 61.0, 73.0])
(90, [79.0, 74.0, 67.0, 73.0])
(120, [76.0, 77.0, 65.0, 73.0])
```

When this program is run with `./main.py resources/sensors-no-label.txt`, the first five lines of the output will be as follows:
```
(0, [65.0, 68.0, 54.0, 63.0])
(30, [76.0, 75.0, 65.0, 71.0])
(60, [77.0, 77.0, 61.0, 73.0])
(90, [79.0, 74.0, 67.0, 73.0])
(120, [76.0, 77.0, 65.0, 73.0])
```
