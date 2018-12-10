import logging
import datetime
import time

from data_api.accounts import AccountsAPI

logger = logging.getLogger(__name__)

accounts_api = AccountsAPI()

def get_transactions(address, start=None, end=None, timeframe_days=None, marker=None, result=[], type=None):
    if timeframe_days is not None and timeframe_days > 0 and start is None and end is None:
        start = (datetime.datetime.now() + datetime.timedelta(-timeframe_days))
        end = datetime.datetime.now()

    data = accounts_api.account_transactions_json(address, start=start, end=end, marker=marker, type=type)

    if 'transactions' in data:
        result.extend(data['transactions'])
    else:
        logger.error(data)
    # logger.info(len(result))

    if 'marker' in data and len(data['marker']) > 0:
        time.sleep(30)
        get_transactions(address, start, end, timeframe_days, data['marker'], result=result, type=type)

    return result
