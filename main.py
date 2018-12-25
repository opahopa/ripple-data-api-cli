import logging

# import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go


from settings.config import *
from services.accounts_tools import get_transactions
from services.data_utils import group_transactions_by_hour
from models.enum import TransactionTypes


logger = logging.getLogger(__name__)

if __name__ == '__main__':
    transactions = get_transactions('rDsbeomae4FXwgQTJp9Rs64Qg9vDiTCdBv', timeframe_days=30, type=TransactionTypes.Payment.name)
    logger.info(len(transactions))

    datetime_count_series = group_transactions_by_hour(transactions, amount_limit=20000)

    x = [e['datetime'] for e in datetime_count_series]
    y = [e['count'] for e in datetime_count_series]
    #
    # plt.plot(x,y)
    # plt.show()

    data = [go.Scatter(
        x=x,
        y=y)]

    plotly.offline.plot(data, filename='bitstamp_payment_20000_30d.html', auto_open=True)