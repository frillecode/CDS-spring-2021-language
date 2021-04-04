# Assignment 4
The structure of the files belonging to this assignment is as follows:
  - Data: _../../data/assignment4/_  
  - Code: _network.py__  
  - Results: _out/_  


### Cloning repo and installing dependencies 
To run the script, I recommend cloning this repository and installing relevant dependencies in a virtual ennvironment:

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

### Running script
After updating the repo (see above), you can run the .py-file from the command-line by writing the following:
``` bash
$ cd CDS-spring-2021-language
$ source frille-lang/bin/activate
$ cd src/assignment4
$ python3 network.py
```

This script takes a weighted edgelist as an input and has the possibility of specifying a cut-off value for weights of node pairs to include in the analysis and visualization. To specify the weighted edgelist and/or cut-off value run:
```bash
$ python3 network.py -we {path to weighted edgelist}
```
or 
```bash
$ python3 network.py -we {path to weighted edgelist} -c {cut-off value}
```

In the '../../data/assignment4/' folder I have provided an example of a weighted edgelist which you can use to test the script - or you can upload and use your own. In the 'out/' folder you can find the output from running the script with the example weighted edgelist and a cut-off value of 10 (i.e. the output from running ```python network.py -we ../../data/weighted_edgelist_test.csv -c 10``` in the command-line).

For more information, run:
```bash
$ python3 network.py --help
```






