<h1 align="center">dslr</h1>
<h2 align="center">Data science x Logistic regression</h2>

<p align='center'>
A 42 school project, from the machine learning / artificial intelligence branch.
 </p>

## Purpose
>A quick project to carry out a One-vs-All logistic regression on a dataset containing Hogwarts students.
>Data statistical analysis and visualization must be performed prior to model training.
>The goal is to create a Sorting Hat model using students marks and others characteristics to assign them to one of the four houses.

## Programs

### 🧙‍♀️ dslr_interative.py
```python3 dslr_interactive.py```

A terminal interactive scenario involving the famous headmistress, McGonagall, and performing all programs presents in this file (except for ```logreg_finetune.py```) . The user can choose to explains what is going on to the headmistress, which will display partial explanations for each program.

<p align='center'>
 <img width= '350' align='center' src='https://user-images.githubusercontent.com/67599180/194900103-66c28466-2930-44a4-94c8-d0f003784cdd.gif' alt='animated'>
</p>

<p align='center'>
 <i align='center'>Project screen capture of interactive mode</i>
</p>

### 🧮 describe.py
```python3 describe.py dataset_filepath```

A program which take as argument the filepath to a dataset to analyze and output corresponding statistical informations.
The goal is to reproduce the describe function of sklearn.
Statistical informations displayed: Count, mean, standard deviation, minimum, first quartile, median, third quartile, maximum, mode, range, interquartile range and number of outliers.

### 📊 histogram.py
```python3 histogram.py```
```python3 histogram.py -expl```

A program to display an histogram of marks distribution for each subject and each Hogwarts house.
The goal was to answer the question "Which subject at Hogwarts is homogeneously distributed between the four houses ?".
With ```-expl``` argument, explanations from the interactive scenario are displayed. 

<p align='center'>
 <img width= '700' align='center' src='https://user-images.githubusercontent.com/67599180/194900426-d29fa66b-db50-44ab-8f6b-80a02d745a35.png' alt='animated'>
</p>
<p align='center'>
 <i align='center'>Project screen capture</i>
</p>

### 📏 scatter_plot.py
```python3 scatter_plot.py```

A program to display a scatter plot of marks distribution for each pair of subjects, and each Hogwarts house.
The goal was to find the two most similars subjects.
With ```-expl``` argument, explanations from the interactive scenario are displayed. 

<p align='center'>
 <img width= '700' align='center' src='https://user-images.githubusercontent.com/67599180/194900432-d42f949e-4c10-4aec-882e-ffd65df64e54.png' alt='animated'>
</p>
<p align='center'>
 <i align='center'>Project screen capture</i>
</p>

### 📐 pair_plot.py
```python3 scatter_plot.py```

A program to display a pair plot of marks distribution of all Hogwarts lessons subjects, for all Hogwarts house.
The goal was to choose useful features to train our model on.
With ```-expl``` argument, explanations from the interactive scenario are displayed. 

<p align='center'>
 <img width= '700' align='center' src='https://user-images.githubusercontent.com/67599180/194900436-d0afbc0f-bdd8-42e8-933c-7a5409bf481d.png' alt='animated'>
</p>
<p align='center'>
 <i align='center'>Project screen capture</i>
</p>

### 🏋 logreg_train.py
```python3 logreg_train.py dataset_filepath```

A program to train our One-vs-All model on a correct Hogwarts dataset (```dataset_train.csv```) taken as argument.
The goal was to reach an accuracy of 98%.
Obtained weights are saved into ```thetas.npz```.
With ```-expl``` argument, explanations from the interactive scenario are displayed. 

### 🔮 logreg_predict.py
```python3 logreg_predict.py dataset_filepath```

A program to attribute Hogwarts' students in one of the four houses.
It takes a correct dataset as argument (```dataset_test.csv```), as well as a weights file (```thetas.npz```).
Predictions are saved into ```houses.csv```.
With ```-expl``` argument, explanations from the interactive scenario are displayed. 

### 📈 logreg_finetune.py
```python3 logreg_finetune.py```

A bonus program, to help find good hyperparameters to use as default value inside ```logreg_train.py```.
It trains the One-Vs-All model with randomly chosen hyperparameters and output the mean of ten differents training (with potential differents randomly initialized weights) with those hyperparameters.
100 experiments are run on the same training and testing sets. Results and hyperparameters values of those experiments are registered in ```experiments.csv```.
At the end of the program, median or mode of hyperparameters values helpful to reach best accuracy are displayed.

## Logistic regression details
### Available optimizations
- RMSprop
- Momentum
- Adam
- Learning rate decay
- Mini-batch or stochastic gradient descent

### Available regularizations
- L2 regularization
- Early stopping

## Available weights initializations
- Zeros
- Random small numbers (0-1)
- He initialization

### Available hyperparameters
- Max iter = Number of epochs
- Alpha = Learning rate
- Beta 1 = Value for momentum / Adam
- Beta 2 = Value for RMSprop / Adam
- Lambda = Value for L2 regularization
- Decay = Learning rate decay
- Decay interval = Interval to perform learning rate decay
- Epsilon = Small number to avoid computation problem in RMSprop / Adam
- Batch size = Size of a batch  (1 = stochastic < mini-batch < max size = batch)


## Language used
Python :snake:
<i>
Why ? Because it's the main language used in data science and machine learning nowadays.
 </i>


## Libraries used
- NumPy (version: 1.21.5)
- pandas (version 1.5.0)
- matplotlib (version 3.5.1)
- sklearn (version 1.1.2)
- playsound (version 1.3.0)
- argparse (version 1.1)

Note that seaborn could have been used for ```pair_plot.py``` but, as 42 restrict the quantity of memory per student, I choose to use solely matplotlib for visualization.

 


