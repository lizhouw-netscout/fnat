#!/usr/bin/env python

from testconfig import config

def remove_quotation(str_param):
    str_len = len(str_param)
    if str_len > 1:
        if (str_param[0] == '\'' and str_param[str_len - 1] == '\'') or \
           (str_param[0] == '"' and str_param[str_len - 1] == '"'):
            return str_param[1:str_len - 1]
    return str_param

def cfg(cfg_name):
    return remove_quotation(config[cfg_name])
