# Analytics with Pandas and Jupyterlab

## Follow-Along tutorial to get you started.

![Poster](img/cover2019.jpg)

Pandas is the Swiss-Multipurpose Knife for Data Analysis in Python. With Pandas dealing with data-analysis is easy and simple but there are some things you need to get your head around first as Data-Frames and Data-Series. 

The tutorial provides a compact introduction to Pandas for beginners for I/O, data visualisation, statistical data analysis and aggregation within Jupiter notebooks.

### Binder
Run Jupyterlab in the cloud, requires internet access.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/alanderex/pydata-pandas-workshop/master?urlpath=lab)

### Installation

#### Local Installation

Copy this repository to your computer
```
# get this repository
git clone https://github.com/alanderex/pydata-pandas-workshop.git
cd pydata-pandas-workshop
```

Make sure to update to the latest vesion just when the training starts:
````bash
git pull
````


Having [Anaconda](https://www.continuum.io/downloads) installed simply create your ENV with 

```bash
# install working environment with conda
conda env create -n pydata-pandas-workshop -f environment.yml

# environment should be activated now
# if not type: source activate pydata-pandas-workshop
```
In case the installation via file fails, simply:
```bash
conda env create -n pydata-pandas-workshop python=3.6
source activate pydata-pandas-workshop
conda install pandas jupyterlab xlrd xlsxwriter dask seaborn -y
```

Alternatively you can also [create a python virtual enviroment](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/) and 
```bash
pip install -r requirements.txt
```


If you don't want to use anaconda, you can use python3 and 
``` 
pip install pandas jupyter barnum numpy matplotlib xlsxwriter seaborn bokeh jupyter parquet dask
``` 
(at your own risk)

### Start Juypterlab
```bash
jupyter lab
# paste the url displayed in your browser, if it doesn't open anyway:
# http://localhost:8888/lab
```  



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

#### Data Visualisation

 * plot your data directly into your notebook

#### Peek Into Statistical Data Analysis & Aggregation

  * Merging
  * Multi-Index
  * DateTime Index
  * Resampling
  * Pivoting

#### Scaling and Optimizing

  * Faster file I/O with Parquet
  * Scaling and Distributing with Dask


