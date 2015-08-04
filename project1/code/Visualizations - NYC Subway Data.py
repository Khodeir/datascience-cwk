
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import pandas


# In[2]:

from ggplot import *


# In[3]:

turnstile_weather = pandas.read_csv('improved-dataset/turnstile_weather_v2.csv')


# In[4]:

totals = turnstile_weather.copy()
d_rain = totals[totals['rain']==1].reset_index()
d_norain = totals[totals['rain']==0].reset_index()
# rain_by_time = d_rain.groupby('time').mean().reset_index()
# norain_by_time = d_norain.groupby('time').mean().reset_index()


# In[7]:

plot = ggplot(aes(x="ENTRIESn_hourly"), data=d_norain) +            geom_histogram(color="red", fill='red', alpha=0.5, binwidth=200) +            geom_histogram(color="blue", fill='blue', alpha=0.5, data=d_rain, binwidth=200) +            ggtitle('Histogram of hourly entries for rainy (blue) and dry (red) times.')
print plot


# In[14]:

totals = turnstile_weather.copy()
d_rain = totals[totals['rain']==1].reset_index()
d_norain = totals[totals['rain']==0].reset_index()
plot = ggplot(aes(x='ENTRIESn_hourly'), data=d_norain) +         geom_density(color='red', fill='red', alpha=0.5) +         geom_density(color='blue', fill='blue', alpha=0.5, data=d_rain) +         ggtitle('Density of hourly entries for rainy (blue) and dry (red) times.')

print plot


# In[16]:

# this plot shows the ridership for different units, for raining vs dry 
totals = turnstile_weather.copy()
d_rain = totals[totals['rain']==1].groupby('UNIT',as_index=False)["ENTRIESn_hourly"].mean()
d_norain = totals[totals['rain']==0].groupby('UNIT',as_index=False)["ENTRIESn_hourly"].mean()

plot = ggplot(aes(x='UNIT',y='ENTRIESn_hourly'), data=d_rain) +         geom_bar(stat='identity', color='blue',fill='blue',alpha=0.5) +         geom_bar(stat='identity', color='red',fill='red',alpha=0.5, data=d_norain) +         ggtitle('Mean ridership per unit for rainy (blue) vs dry (red) times.') +         scale_x_discrete(labels=['' for i in range(240)])
print plot


# In[17]:

totals = turnstile_weather.copy()
# bin temp into boxes of 2.5 degrees
totals['meantempi'] = totals['meantempi'].map(lambda x: int(x) - int(x)%2.5 + 1.25)
totals = totals.groupby(['meantempi','rain'], as_index=False)['ENTRIESn_hourly'].mean()
d_rain = totals[totals['rain']==1].reset_index()
d_norain = totals[totals['rain']==0].reset_index()

plot = ggplot(aes(x='meantempi',y='ENTRIESn_hourly'), data=d_rain) +         geom_point(color='blue',alpha=0.5) +         geom_point(color='red',alpha=0.5, data=d_norain) +         ggtitle('Ridership vs mean temp for rainy (blue) vs dry (red) times.')
print plot


