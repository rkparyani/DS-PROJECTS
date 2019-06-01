# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:23:44 2019

@author: Ritesh
"""

# Import Libraries - TBD - To create a dataframe and import based on the flag based on the problem on hand
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
%matplotlib inline

# Declare Properties - All the property values to be used across. One place to update to govern the model functionality
typ = 'regression'  # Type of problem in hand based on response type
file = 'D:\RITESH\\Data Science\\GIT WD\\SDS CAR PRICES  PREDICTION\\data\\automobile.csv' #

featurelist = ['symboling',
'normalizedlosses',
'make',
'fueltype',
'aspiration',
'numofdoors',
'bodystyle',
'drivewheels',
'enginelocation',
'wheelbase',
'length',
'width',
'height',
'curbweight',
'enginetype',
'numofcylinders',
'enginesize',
'fuelsystem',
'bore',
'stroke',
'compressionratio',
'horsepower',
'peakrpm',
'citympg',
'highwaympg',
'price']

removecolumns = []





#  Variable Declaration/Update

libnames = {'names':['numpy','pandas','matplotlib.pyplot','seaborn','warnings','scipy','scipy.stats','sklearn.linear_model','sklearn.ensemble','sklearn.kernel_ridge','sklearn.pipeline','sklearn.preprocessing','sklearn.base','sklearn.model_selection','sklearn.metrics','os'],
            'import':['','','','','','stats','norm,skew','ElasticNet, Lasso,  BayesianRidge, LassoLarsIC, LinearRegression','RandomForestRegressor,  GradientBoostingRegressor','KernelRidge','make_pipeline','RobustScaler','BaseEstimator, TransformerMixin, RegressorMixin, clone','KFold, cross_val_score, train_test_split','mean_squared_error',''],
            'as':['np','pd','plt','sns','wn','','','','','','','','','','','os'],
            'type':['common','common','common','common','common','common','common','regression','regression','regression','common','common','common','common','regression','common']}   # Create a dictionary object to define all the class names and objects along with alias to be imported at once 

lib = pd.DataFrame(libnames)



import general

        
#        
#class generalvisualizations(object):
#    def __init__(self,ln,ty,file):
#    self.ln = ln
#    self.ty = ty
#    self.file = file

#    def variability(self):
        


#   MODEL
#	1. Import the libraries
gf = generaloperations(lib,typ,file)
gf.importlib()

# Import the data
df = gf.importfile(featurelist)
df.head()

# Replace any other identified values to NA
x = gf.replacebyna(df,'?')
type(x)

# Change the dtypes
# Divide into Categorical and continuous
df.isna().sum()


x = (df=='?').sum()
x = x[x>0]
type(x)
x.index
nafeats = x.index.values
(df[nafeats]=='?').sum()
df.replace('?',np.NaN)


x.index.values.tolist
np.take(x,[1,2,1])
x = pd.DataFrame(x)
x[x[[0]]==True].skipna
df.isna().any()


