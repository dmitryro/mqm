# -*- coding: utf-8 -*-
from cssmin import cssmin
from compressor.filters import FilterBase


class CSSMinFilter(FilterBase):
    def output(self, **kwargs):
        return cssmin(self.content)
