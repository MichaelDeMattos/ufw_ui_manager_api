# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from prometheus_client import Gauge


logger = logging.getLogger(__file__)
level = logging.DEBUG
logging.basicConfig(encoding="utf-8", level=level)
timed_step = Gauge(
    "timed_step", "Timed Step", ["step", "type"])


class TimedAppSteps(object):
    def __init__(self, description: str, logger_class: str = "INFO"):
        self._start = None
        self._end = None
        self._total_seconds = None
        self._description = description
        logger.setLevel(logger_class)
        self._level = logger.level

    def __create_msg(self, action: str, *args):
        if action == "__enter__":
            logger.log(
                level=self._level,
                msg={
                    "action": self._description,
                    "started_at": self._start.strftime("%Y-%m-%d %H:%M:%S"),
                },
                *args,
            )
        elif action == "__exit__":
            logger.log(
                level=self._level,
                msg={
                    "action": self._description,
                    "ended_at": self._end.strftime("%Y-%m-%d %H:%M:%S"),
                    "total_seconds": self._total_seconds,
                },
                *args,
            )

    def __enter__(self):
        self._start = datetime.now()
        self.__create_msg(action="__enter__")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._end = datetime.now()
        self._total_seconds = (self._end - self._start).total_seconds()
        self.__create_msg(action="__exit__")
        timed_step.labels(
            step=self._description,
            type="tracer").set(value=self._total_seconds)
