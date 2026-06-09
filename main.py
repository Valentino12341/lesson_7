#types of machine learning      supervised [for example a picture with a lable attached to it ]  unsupervised [for example a lot of pictures with no lables and the compuiter needs to group them himself] and reinforcment[for example working with rewards like if you do this its correct ] 
# 
#  recommendation[for example the user looks at a lot off cat pictures and f wil keep showing cat pictures ]  classificatiiom[there a lot of pictures and the user asks for only  bananas or smth and it gives bannanan pictures ]      regression [for exaple to find the weather tommorow it looks at a lot of cources and it gets close to the actual number but not exactly so it gives for example between 20 and 22 degrees ]

#all steps of machine learning 
 # A getting the data and loading it in to the program 
 # B prepare the datta and look if the isnt data missing and change int in to strings of 1 0 for example 
 # C alalyse the data so that you can define the input and what the output is 
 # E train the moddle use for example 75 % of the data to train the moddle and 25 % to test if it works 
 # F select de machine learning algorithm and perform the training of the programm 
 # G look at predicions and compare to what the program did to look at how acurate it is 



import numpy as np
import pandas as pd
data = pd.read_csv("lesson_7/Data.csv")
print(data.info())


# data analysis  
x = data.iloc[:, :-1].values    # the [:, :-1]means get every collum exeptthe -1th  so untill the -1th
y = data.iloc[:,-1].values      # means only get the -1th collum

print("Features : \n",x)
print("Target : \n",y)

# data preprocessing

# replacing the missing value in salary and in age with the avrage{mean} of the collum 
from sklearn.impute import SimpleImputer

