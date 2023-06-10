#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[34]:


df1 =pd.read_csv(r'C:\Users\ayu\Downloads\product_detail.csv')
df1.head()


# In[35]:


df1.info()


# In[36]:


df1.describe()


# In[37]:


df2 = pd.read_csv(r'C:\Users\ayu\Downloads\products_catalog.csv')
df2.head()


# In[38]:


df2.rename({'ID':'ProductID'}, axis = 1,inplace=True)
df2.head()


# In[ ]:


df = df('Gender','Price


# In[39]:


df = pd.merge(df1,df2,on="ProductID",how='left')
df.head()


# In[40]:


df.duplicated().sum()


# In[41]:


df.isna().sum()


# In[83]:


pd.value_counts(df['ProductBrand'])


# In[85]:


df['ProductBrand'].nunique()


# In[44]:


# Filling the null values by Others
df=df.fillna("Others")


# In[45]:


# Removing leading spaces from PrimaryColor column
df['PrimaryColor']=df['PrimaryColor'].str.strip()


# In[46]:


df.rename({'Price (INR)':'Price'},axis=1,inplace=True)
df.head()


# In[47]:


df.Gender.value_counts()


# In[48]:


print("max price : ",df['Price'].max())
print("min price : ",df['Price'].min())
print("mean price : ",df['Price'].mean())


# In[49]:


sns.countplot(data=df,x='Gender')


# In[50]:


sns.barplot(data=df,x='Gender',y='Price')


# In[51]:


df.groupby('Gender')['ProductID'].count().plot.pie(autopct="%1.1f%%")


# In[52]:


sns.pairplot(df,hue='Gender')
plt.show()


# In[53]:


# By analyzing the Gender column we can predict the most active Gender.
# We can also predict the brand which is mostly choose by people.
# We Can also predict the most Trending color or Brand.
# According to Gender which gender has the most brand.


# In[54]:


df.loc[df['Gender']=='Women','NewGender'] = 'Women'
df.loc[df["Gender"]=='Girls',"NewGender"]= 'Women'
df.loc[df['Gender']=='Men', "NewGender"] = 'Men'
df.loc[df['Gender']=='Boys',"NewGender"] = "Men"
df.loc[df['Gender']=='Unisex' , "NewGender"] = 'Unisex'
df.loc[df['Gender']=='Unisex Kids','NewGender']='Unisex'
df.head(2)


# In[55]:


df.groupby('NewGender')['ProductID'].count().plot.pie(autopct="%1.1f%%")


# In[56]:


sns.barplot(data=df,x='NewGender',y='Price')


# In[57]:


# Top 10 ProductBrand
df.ProductBrand.value_counts()[:10].plot(kind='bar',title="Top 10 Popular Brand",color='g')


# In[58]:


# Most demanding colors
df.groupby('PrimaryColor')['ProductID'].count().plot.bar()


# In[59]:


# Most Expensive Brands
df1=df.groupby('ProductBrand')['Price'].mean().sort_values(ascending=False).head(10)
df1.plot.bar()


# In[60]:


# Creating a new column DescriptionLength
df["DescriptionLength"] = df["Description"].apply(lambda n: len(n.strip()))


# In[61]:


df.info()


# In[62]:


df.isna().sum()


# In[63]:


df.groupby("NewGender").agg(TotalRecords=("ProductID","size"),AvgLength=("DescriptionLength","mean"))


# In[33]:


## DescriptionLength doesn't seem to play a key role in making decision because it doesn't effect avg.price or no. of Records.


# In[33]:


### Conclusion-
# 1. According to Gender data Women have the most data.
# 2. According to NewGender Men has the more data. 
# 3. The Total number of ProductBrand  is 677.
# 4. Indian terrain is the top brand.
# 5. Blue is the most favourite PrimaryColor
# 6. Most Expensive Brand is Garmin.

