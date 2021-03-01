### Weekly assignments
Each week I will upload my answers to the given assignments here under the following names:
- __W1:__ _word\_counts.ipynb_  
- __W2:__ _collocation.py_  
- __W4:__ script: _sentiment.py_ ; plots: _sentiment_7-days.jpg_ and _sentiment_30-days_ ; interpretation: _sentiment_interpretation.txt_

The output files from the scripts can be found in the folder _out_.  

__Cloning repo and installing dependencies__  
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

__Running scripts__  
After updating the repo (see above), you can run the .py-files from the command-line by writing the following:
``` bash
$ cd CDS-spring-2021-language
$ source frille-lang/bin/activate
$ cd src
$ python3 {filename].py
```
