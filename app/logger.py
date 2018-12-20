import logging
import traceback

from .database import db
from app.models.log import Log


class DbLogHandler(logging.Handler):
    def emit(self, record):
        trace = None
        created_by = 'System'

        exc = record.__dict__['exc_info']
        if exc:
            trace = traceback.format_exc()

        if 'created_by' in record.__dict__:
            created_by = record.__dict__['created_by']

        log = Log(
            level=record.__dict__['levelname'].lower(),
            message=record.__dict__['message'],
            trace=trace,
            created_by=created_by
        )

        try:
            db.session.add(log)
            db.session.commit()
        except Exception as ex:
            print("Cannot connect to DB while logging.", ex)
            print("Original Error: ", log)


# create logger
logger = logging.getLogger('workflow-logger')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# create database handler
dbHandler = DbLogHandler()
dbHandler.setLevel(logging.DEBUG)

# add ch to logger
logger.addHandler(dbHandler)
