import itertools
import logging
# import matplotlib.pyplot as plt
from collections import Counter

from datetime import datetime, time
from dateutil.parser import parse

logger = logging.getLogger(__name__)


def group_transactions_by_hour(transactions, amount_limit=None):
    result = []

    # for timestamp, grp in itertools.groupby(transactions, lambda x: (datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S%z'))):
    for timestamp, grp in itertools.groupby(transactions,
                                            lambda x: datetime.combine(parse(x['date']),
                                                                       time(parse(x['date']).hour, 0, 0, 0))):

        group = list(grp)
        result_group = []
        if amount_limit:
            for t in group:
                try:
                    if int(t['tx']['Amount']) // 1000000 < amount_limit:
                        result_group.append(t)
                    # else:
                        # logger.info('Higher!: {}'.format(t['tx']['Amount']))
                except KeyError:
                    logger.error(t['tx'])
        else:
            result_group = group

        result.append({'datetime': timestamp, 'count': len(result_group)})

    return result
