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

An interactive scenario involving the famous headmistress, McGonagall, and performing all programs presents in this file (except for ```logreg_finetune.py```) . The user can choose to explains what is going on to the headmistress, which will display partial explanations for each program.

### 🧮 describe.py
```python3 describe.py dataset_filepath```

A program which take as argument the filepath to a dataset to analyze and output corresponding statistical informations.
The goal is to reproduce the describe function of sklearn.
Statistical informations displayed: Count, mean, standard deviation, minimum, first quartile, median, third quartile, maximum, mode, range, interquartile range and number of outliers.

### 📊 histogram.py
```python3 histogram.py```
```python3 histogram.py -expl```

A program to display an histogram of marks distribution for each subject and each Hogwarts house.
With ```-expl``` argument, explanations from the interactive scenario are displayed. 

<p align='center'>
 <img width= '700' align='center' src='https://user-images.githubusercontent.com/67599180/194900426-d29fa66b-db50-44ab-8f6b-80a02d745a35.png' alt='animated'>
</p>
<p align='center'>
 <i align='center'>Project screen capture</i>
</p>

### :100: accuracy.py
```python3 accuracy.py```

A program which explains the differents accuracy measures available and perform it for our current data set.



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

 
<p align='center'>
 <img width= '350' align='center' src='https://user-images.githubusercontent.com/67599180/194900103-66c28466-2930-44a4-94c8-d0f003784cdd.gif' alt='animated'>
</p>

<p align='center'>
 <i align='center'>Project screen capture of interactive mode</i>
</p>



<p align='center'>
 <img width= '700' align='center' src='https://user-images.githubusercontent.com/67599180/194900432-d42f949e-4c10-4aec-882e-ffd65df64e54.png' alt='animated'>
</p>

<p align='center'>
 <img width= '700' align='center' src='https://user-images.githubusercontent.com/67599180/194900436-d0afbc0f-bdd8-42e8-933c-7a5409bf481d.png' alt='animated'>
</p>
