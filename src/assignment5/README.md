# Assignment 3
The structure of the files belonging to this assignment is as follows:
  - Data: _../../data/assignment5/_  
  - Code: _LR_philosophicalTexts.py__  
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
$ cd src/assignment5
$ python3 LR_philosophicalTexts.py
```

## Description of dataset and interpretation of results
I chose to analyse a [dataset](https://www.kaggle.com/christopherlemke/philosophical-texts?select=sentences.csv) consisting of text from different philosophers to see whether structures of the texts could be used the predict the author. The file that I chose is a collection of sentences extracted from the text files along with a column indicating the author of the text.  

I trained a logistic regression classification model to predict the author of a philosophical text based on a tfid-vector of the words in the texts. Because the data was sparse, I scaled the data using the inbuilt MaxAbsScaler() from sklearn (dividing by max value for each feature to get values between -1 and 1), which is a solution suggested in the [scikit-learn documentation](https://scikit-learn.org/stable/modules/preprocessing.html). I played around with some different choices for analysis (e.g. the thresholds for removing common/uncommon words) to see how this would affect the performance of the model. Setting a lower threshold for removing rare words (those that appear in less than 0.1% of the texts) seemed to increase the accuracy of the model. However, the most succesful model had an accuracy of 0.6 - just above chance - indicating that it was not possible to predict author from a tfid-vector of words in the texts. The f1-scores ranged between 0.39 to 0.74 for the different authors, implying that the model differed quite a lot in how successful it was for predicting different authors. You can find a confusion matrix and classifier metrics for this model in the _out_-folder. To validate the results, I performed cross-validation to get average performance using different test-train splits. The results of this can also be found in the _out_-folder. Inspecting the learning curves, it seems that the model might suffer from a problem of underfitting.  
