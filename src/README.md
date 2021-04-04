## Weekly assignments
Each week I will upload my answers to the given assignments here under the following names:
- __Assignment 1:__  
  - Data: _../data/assignment1/_  
  - Code: _assignment1/word\_counts.ipynb_  
  - Results: _assignmen11/out/_  
- __Assignment 2:__  
  - Data: _../data/assignment2/_  
  - Code: _assignment2/collocation.py_  
  - Results: _assignmetn2/out/_
- __Assignment 3:__  
  - Data: _../data/assignment3/_  
  - Code: _assignment3/sentiment.py_
  - Results: _assignmetn3/out/_    
- __Assignment 4:__  
  - Data: _../data/assignment4/_  
  - Code: _assignment4/network.py_  
  - Results: _assignmetn4/output/_ and  _assignmetn4/viz/_  
- __Assignment 5:__  
  - Data: _../data/assignment5/_  
  - Code: _assignmetn5/LR_philosophicalTexts.py_  
  - Results: _assignmetn5/out/_   

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
$ cd src/assignment{number}
$ python3 {filename}.py
```
