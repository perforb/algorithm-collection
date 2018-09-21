# -*- coding: utf-8 -*-


class Stack:

    def __init__(self, length):
        self._top = 0
        self._elements = [None] * length

    def push(self, element):
        self._top += 1
        self._elements[self._top] = element

    def pop(self):
        if self._top <= 0:
            raise RuntimeError('No elements.')
        element = self._elements[self._top]
        self._top = (self._top - 1) if self._top > 0 else 0
        return element
