import datetime
import enum

from ..database import db


class LogLevel(enum.Enum):
    debug = "DEBUG"
    info = "INFO"
    warn = "WARN"
    error = "ERROR"
    critical = "CRITICAL"

    def __str__(self):
        return str(self.value)


class Log(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.Enum(LogLevel))
    message = db.Column(db.String)
    trace = db.Column(db.String)
    created_by = db.Column(db.VARCHAR(80))
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)

    def __init__(self, level=None, message=None, trace=None, created_by=None):
        self.level = level
        self.message = message
        self.trace = trace
        self.created_by = created_by
        self.created_at = datetime.datetime.utcnow()

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.message)
