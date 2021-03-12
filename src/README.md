## Weekly assignments
Each week I will upload my answers to the given assignments here under the following names:
- __Assignment 1:__   
  - Code: _word\_counts.ipynb_  
- __Assignment 2:__ 
  - Code: _collocation.py_  
  - Results: _out/assignment2/collocates.csv_
- __Assignment 3:__ 
  - Code: _sentiment.py_
  - Results: _out/assignment3/sentiment_7-days.jpg_ , _out/assignment3/sentiment_30-days.jpg_ , _out/assignment3/sentiment_interpretation.txt_  
- __Assignment 4:__
  - Code: _network.py__  
  - Results: _out/assignment4/output/centrality.csv_ , _out/assignment4/viz/network.png_  

### Cloning repo and installing dependencies 
To run the scripts, I recommend cloning this repository and installing relevant dependencies in a virtual ennvironment:

```bash
$ git clone https://github.com/frillecode/CDS-spring-2021-language.git
$ cd CDS-spring-2021-language
$ bash ./create_venv.sh
````
If you run into issues with some libraries/modules not being installed correctly when creating the virtual environment, install these manually by running the following:  
```bash
$ cd CDS-spring-2021-language
$ source frille-lang/bin/activate
$ pip install {module_name}
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
