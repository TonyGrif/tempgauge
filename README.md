# Tempgauge
This python project utilizes piecewise linear interpolation and
least-squares approximation to analyze CPU temperature readings over time.

## Requirements
* [Python 3.9+](https://www.python.org/)
* [NumPy](https://numpy.org/)

## Running Instructions
This program can be run with the following command: `./main.py [text file]`
in which the text file contains CPU temperature data in the following format
with each new line signifying a new reading at a different time:
```
[core1 temp] [core2 temp] ... [coreN temp]
...
[core1 temp] [core2 temp] ... [coreN temp]
```

If this program is run without any arguments, the following usage error
message will be outputted: `usage: cpu-temperature [-h] txt_file`

Invalid text file formatting will not be checked for and will result in undefined behavior.

## Sample Execution & Output
When this program is run with `./main.py resources/sample.txt`, four output
files will be created, one for each core following the naming convention of `core-{core_number}.txt`.
As an example, `core-0.txt` will contain the following:
```
0      <= x <=     30; y = 61.0000 + 0.6333; interpolation
30     <= x <=     60; y = 98.0000 + -0.6000; interpolation
60     <= x <=     90; y = 20.0000 + 0.7000; interpolation
90     <= x <=    120; y = 128.0000 + -0.5000; interpolation
0      <= x <=    120; y = 67.4000 + 0.0567; least-squares
```

When this program is run with `./main.py resources/sensors-with-label.txt`,
four output files with the aforementioned naming convention will be created.
`core-0.txt` will be populated with the following lines:
```
0      <= x <=     30; y = 65.0000 + 0.3667; interpolation
30     <= x <=     60; y = 75.0000 + 0.0333; interpolation
60     <= x <=     90; y = 73.0000 + 0.0667; interpolation
90     <= x <=    120; y = 88.0000 + -0.1000; interpolation
120    <= x <=    150; y = 68.0000 + 0.0667; interpolation
...
0      <= x <=  30690; y = 83.2340 + -0.0008; least-squares
```
