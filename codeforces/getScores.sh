#!/bin/bash
python3 resultCalculator.py input.csv $1
python3 ranksToScore.py
cat scores.csv
