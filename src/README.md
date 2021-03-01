## Weekly assignments
Each week I will upload my answers to the given assignments here under the following names:
- __Assignment 1:__   
  - Code: 
    - _word\_counts.ipynb_  
- __Assignment 2:__ 
  - Code: 
    - _collocation.py_  
  - Results: 
    - _out/collocates.csv_
- __Assignment 3:__ 
  - Code: 
    - _sentiment.py_
  - Results: 
    - _out/sentiment_7-days.jpg_
    - _out/sentiment_30-days_
    - _sentiment_interpretation.txt_

### Cloning repo and installing dependencies 
To run the scripts, I recommend cloning this repository and installing relevant dependencies in a virtual ennvironment:

```bash
$ git clone https://github.com/frillecode/CDS-spring-2021-language.git
$ cd CDS-spring-2021-language
$ bash ./create_frille-lang_venv.sh
````
As there are some issues with installing certain libraries in the virtual environment, these needs to installed manually by running the following in the terminal:  
```bash
$ cd CDS-spring-2021-language
$ source frille-lang/bin/activate
$ pip install spacy==2.3.5
$ pip install spacytextblob
$ pip install pandas
$ pip install matplotlib
$ python -m spacy download en_core_web_sm
$ deactivate
```

### Running scripts
After updating the repo (see above), you can run the .py-files from the command-line by writing the following:
``` bash
$ cd CDS-spring-2021-language
$ source frille-lang/bin/activate
$ cd src
$ python3 {filename].py
```
