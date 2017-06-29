# Introduction to Data-Analysis with Pandas

## Follow-Along Tutorial PyData Berlin 2017

Pandas is the Swiss-Multipurpose Knife for Data Analysis in Python. With Pandas dealing with data-analysis is easy and simple but there are some things you need to get your head around first as Data-Frames and Data-Series. 

The tutorial provides a compact introduction to Pandas for beginners for I/O, data visualisation, statistical data analysis and aggregation within Jupiter notebooks.

### Installation

Having [Anaconda](https://www.continuum.io/downloads) installed simply create your ENV with 

```
# get this repository
git clone https://github.com/alanderex/pandas-pydata-berlin-2017

cd pandas-pydata-berlin-2017
# install working environment with conda
conda env create -n pandas-pydata-berlin-2017 -f environment.yml

# environment should be activated now
# if not type: source activate pandas-pydata-berlin-2017

# start juypter notebook
jupyter notebook

# paste the url displayed in your browser, looks like:
# http://localhost:8888/?token=fa08a1f56d3d0fbbdf7d07fec0c39cd471e06501f79a782a
``` 

![alt tag](pic/front.jpeg)

#### A Practical Start: Reading and Writing Data Across Multiple Formats 

* CSV
* Excel
* JSON
* Clipboard
 
* data
    * .info
    * .describe

#### DataSeries & DataFrames / NumPy

* Ode to NumPy
* Data-Series
* Data-Frames

#### Data selection & Indexing

* Data-Series: 
    * Slicing
    * Access by label
    * Index
* Data-Frames: 
    * Slicing
    * Access by label
    * Peek into joining data
* Returns a copy / inplace
* Boolean indexing

#### Operations
    
 * add/substract
 * multiply
 * mention Index but don't go deep

#### Data Visualisation

 * plot your data directly into your notebook

#### Peek Into Statistical Data Analysis & Aggregation



