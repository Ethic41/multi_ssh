#!/usr/bin/env python
# -=-<[ Bismillahirrahmanirrahim ]>-=-
# -*- coding: utf-8 -*-
# @Date    : 2021-06-27 02:06:05
# @Author  : Dahir Muhammad Dahir
# @Description : something cool


from pydantic import validator


def none_validator(field: str):
    return validator(field, allow_reuse=True)(my_none)


def my_none(entry: str):
    if entry == "none":
        return None
    
    else: return entry