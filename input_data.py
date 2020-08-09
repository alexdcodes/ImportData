import sqlite3


def c(value):
    if value.startswith("~"):
        return value.strip('~')