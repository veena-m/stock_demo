from flask import Flask, render_template, request, redirect,json
import get_quandl_data as gqd
import plot_closing_price as pcp

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
  if request.method == 'GET':
     return render_template('InputTicker.html')
  else:
    #request was a POST
    ticker = request.form['ticker']
    if ticker: 
        print ticker
        #get quandl data only if you have a ticker input
        data_df = gqd.get_data_df(ticker)
        if len(data_df):
            #print 'back from quandl_data_df %i' %len(data_df)
            #p = pcp.plot_closing_price(ticker,data_df)
            script, div = pcp.plot_closing_price(ticker,data_df)
            
            return render_template('graph.html', script=script, div=div)

        else:
            return render_template('error.html')
            
    else:
        return render_template('error.html')    

        
if __name__ == '__main__':
  app.run(port=33507)
#  app.run(host='0.0.0.0')
  
  
    