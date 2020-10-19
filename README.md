# Udacity Capstone Project - Customer Segmentation

The following project used datasets supplied from Arvato. The overall aim was to understand the current customer demographic of a mail order company using data from a general population, data from the customer population and data from a prior non-targeted ad campaign using an unsupervised learning model.

The intention would be to use this understanding to inform a future targeted ad campaign that could target fewer people and have the same or greater chances of success. With confidence to this given through a supervised learning model.

The general dataset provided consisted of 366 features that described approximately 1 million individuals from the German population. This dataset was not 'clean' and required a lot of data wrangling in order to be in a position where it would be ready to inform unsupervised and supervised tasks. 

In keeping with the Pareto Principle, this portion of the project took about 80% of the overall project time.

A customer demographic was identified using a knn model and this was used to engineer new features that were used to build an XGBoost classifier model that aimed to predict whether an individual would sign up.

Overall this supervised model had a measured success of:

# Steps to Reproduce

Work was carried out in Jupyter Notebooks locally to keep costs down.

The majority of packages used are provided in the Anaconda environment 'out of the box' notwithstanding XGBoost.

The steps can be reproduced by following the 3 notebooks with the supplied datasets. N.B. due to confidentiality the datasets are not provided publicly. These are supplied through the Udacity Machine Learning Nanodegree as part of the Capstone project.

The following resources are therefore, not provided and would need to be accessed through Udacity:

* Udacity_AZDIAS_052018.csv
* Udacity_CUSTOMERS_052018.csv
* Udacity_MAILOUT_052018_TEST.csv
* Udacity_MAILOUT_052018_TRAIN.csv
* DIAS_Attributes_Values_2017.xlsx
* DIAS_Information_Levels_Attributes_2017_Komplett.xlsx

The order of notebooks to follow is:

- TO BE ADDED

Notebooks were run on a local windows 10 machine with 16GB of RAM and an Intel Core i5-3570k, 3.4GHz CPU. 

Generally resource demands where possible were kept low but in development the kernel and machine did occasionally crash. Note steps were taken to optimise or use accelerators but it is worth keeping these machine specifications in mind when attempting to reproduce.

If the Anaconda or XGBoost are not installed on your machine, the additional steps will need to be taken in order to reproduce:

1. Install the Anaconda suite: https://www.anaconda.com/
2. From the conda prompt, install XGBoost: pip install xgboost
3. From the conda prompt, install Bayesian Optimiser: pip install BayesianOptimization
4. from the conda prompt, install BorutaPy: pip install BorutaPy
5. from the conda prompt, install SHAP: pip install shap
