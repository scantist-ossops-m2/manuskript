#!/usr/bin/env python
# --!-- coding: utf8 --!--

from enum import Enum, unique


@unique
class GoalKind(Enum):
    WORDS = 0
    CHARACTERS = 1


class Goal:

    def __init__(self, value: int = 0, kind: GoalKind = GoalKind.WORDS):
        self.value = 0
        self.kind = kind

    def __str__(self):
        return str(self.value) + " " + self.kind.name.lower()

    @classmethod
    def parse(cls, string: str):
        if string is None:
            return None

        parts = string.split(" ")

        try:
            value = int(parts[0])
            kind = GoalKind[parts[1].upper()] if len(parts) > 1 else GoalKind.WORDS
        except ValueError:
            return None

        return Goal(value, kind)
