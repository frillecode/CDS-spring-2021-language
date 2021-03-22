## Weekly assignments
Each week I will upload my answers to the given assignments here under the following names:
- __Assignment 1:__  
  - Data: _../data/assignment1/_  
  - Code: _word\_counts.ipynb_  
  - Results: _out/assignment1/_  
- __Assignment 2:__  
  - Data: _../data/assignment2/_  
  - Code: _collocation.py_  
  - Results: _out/assignment2/
- __Assignment 3:__  
  - Data: _../data/assignment3/_  
  - Code: _sentiment.py_
  - Results: _out/assignment3/_    
- __Assignment 4:__  
  - Data: _../data/assignment4/_  
  - Code: _network.py__  
  - Results: _out/assignment4/_  

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
