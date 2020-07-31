#!/bin/bash
python3 getranks.py input.csv $1
python3 ranksToScore.py
cat scores.csv
