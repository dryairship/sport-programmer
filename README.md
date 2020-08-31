# Result Calculators for the Sport Programmer of the Month Challenge

## Usage 

1. Download the list of students registered for the contest in the form of a `.csv` file and place it in `./`.

2. run `filter.py` with :

```python
python3 filter.py
```
### You are now setup for the whole month !
3. Contests :
  - move into the folder for the respective competition using `cd`.
  - ### atcoder : 
    - enter your atcoder credenntials in lines `12` and `13` of `scrape.py`
    - Then run the following command to get the scores:
        ```
        ./getScores.sh <contest-id>
        ```
    Example: `./getScores.sh abc171`
  - ### codeforces : 
    - Run the following command to get the scores: 
        ```
        ./getScores.sh <contest-id>
        ```
        Example: `./getScores.sh 1397`
    - The results are calculated and stored in the file `scores.csv` of the respective directories

## Contributors : 

The following students were involved in writing the programs: 

 - Atcoder Rank Calculator: [namangup](https://github.com/namangup)
 - Codeforces Rank Calculator: [abhimanyusethia12](https://github.com/abhimanyusethia12)
 - Ranks to Score Convertor: [AthaSSiN](https://github.com/AthaSSiN)
 - README : [Pramodh-G](https://github.com/Pramodh-G)
