import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
data = ts.get_hist_data('600848',start='2019-05-01',end='2019-05-19')
data = data.sort_index()
xs = [datetime.strptime(d, '%Y-%m-%d').toordinal() for d in data.index]
plt .plot_date(xs, data['open'], 'b-')
plt.gcf().autofmt_xdate()
plt.show()