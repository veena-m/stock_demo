#from bokeh.plotting import figure
#from bokeh.resources import CDN
#from bokeh.embed import file_html

from bokeh.charts import TimeSeries
from bokeh.embed import components 

import pandas as pd

def plot_closing_price(ticker,df):
   
   #print ticker, df
   df['date'] = pd.to_datetime(df['date'])
   df.set_index('date')
        
   plot = TimeSeries(df, x='date', y='closing_price', legend=True, title=ticker , xlabel='Date', ylabel='Closing stock price')
   plot.title.text_font_size = '14pt'
       
   #html = file_html(p, CDN, "bokehplot")
   #return html

   
   script, div = components(plot)
   return script,div 