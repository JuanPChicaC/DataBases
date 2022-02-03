# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:32:14 2022

@author: juanp
"""
import datetime as dt

clients = [
    {'username' : 'JuanPChicaC'},
    {'username' : 'TestingUser'}
    ]


periods = [
    {
     'code' : '1d',
     'time_minutes': int(dt.timedelta(days = 1)/dt.timedelta(minutes = 1)),
     'description' : 'One day of prices historic information'
     },
    {
     'code' : '5d',
     'time_minutes' : int(dt.timedelta(days = 5)/dt.timedelta(minutes = 1)),
     'description' : 'Five days of prices historic information'
     },
    {
     'code' : '1mo',
     'time_minutes' : int(dt.timedelta(days = 30)/dt.timedelta(minutes = 1)),
     'description' : 'One month of prices historic information'
     },
    {
     'code' : '3m',
     'time_minutes' : int(dt.timedelta(days = 90)/dt.timedelta(minutes = 1)),
     'description' : 'Three months of prices historic information'
     },
    {
     'code' : '6m',
     'time_minutes' : int(dt.timedelta(days = 180)/dt.timedelta(minutes = 1)),
     'description' : 'Six months of prices historic information'
     },
    {
     'code' : '1y',
     'time_minutes' : int(dt.timedelta(days = 365)/dt.timedelta(minutes = 1)),
     'description' : 'One year of prices historic information'
     },
    {
     'code' : '2y',
     'time_minutes' : int(dt.timedelta(days = 365*2)/dt.timedelta(minutes = 1)),
     'description' : 'Two years of prices historic information'
     },
    {
     'code' : '5y',
     'time_minutes' : int(dt.timedelta(days = 365*5)/dt.timedelta(minutes = 1)),
     'description' : 'five years of prices historic information'
     },
    {
     'code' : '10y',
     'time_minutes': int(dt.timedelta(days = 365*10)/dt.timedelta(minutes = 1)),
     'description' : 'Ten years of prices historic information'
     }
    ]

intervals = [
    {
     'code' : '1m',
     'time_minutes': int(dt.timedelta(minutes = 1)/dt.timedelta(minutes = 1)),
     'description' : 'One minute records of information'
     },
    {
     'code' : '2m',
     'time_minutes': int(dt.timedelta(minutes = 2)/dt.timedelta(minutes = 1)),
     'description' : 'Two minutes records of information'
     },
    {
     'code' : '5m',
     'time_minutes': int(dt.timedelta(minutes = 5)/dt.timedelta(minutes = 1)),
     'description' : 'Five minutes records of information'
     },
    {
     'code' : '15m',
     'time_minutes': int(dt.timedelta(minutes = 15)/dt.timedelta(minutes = 1)),
     'description' : 'Fifteen records of information'
     },
    {
     'code' : '30m',
     'time_minutes': int(dt.timedelta(minutes = 30)/dt.timedelta(minutes = 1)),
     'description' : 'thirty minutes records of information'
     },
    {
     'code' : '60m',
     'time_minutes': int(dt.timedelta(minutes = 60)/dt.timedelta(minutes = 1)),
     'description' : 'Sixty minutes records of information'
     },
    {
     'code' : '90m',
     'time_minutes': int(dt.timedelta(minutes = 90)/dt.timedelta(minutes = 1)),
     'description' : 'ninety minutes records of information'
     },
    {
     'code' : '1h',
     'time_minutes': int(dt.timedelta(hours = 1)/dt.timedelta(minutes = 1)),
     'description' : 'One hour records of information'
     },
    {
     'code' : '1d',
     'time_minutes': int(dt.timedelta(days = 1)/dt.timedelta(minutes = 1)),
     'description' : 'One day records of information'
     },
    {
     'code' : '5d',
     'time_minutes': int(dt.timedelta(days = 5)/dt.timedelta(minutes = 1)),
     'description' : 'Five days records of information'
     },
    {
     'code' : '1wk',
     'time_minutes': int(dt.timedelta(weeks = 1)/dt.timedelta(minutes = 1)),
     'description' : 'One week records of information'
     },
    {
     'code' : '1mo',
     'time_minutes': int(dt.timedelta(days = 30)/dt.timedelta(minutes = 1)),
     'description' : 'One month records of information'
     },
    {
     'code' : '3mo',
     'time_minutes': int(dt.timedelta(days = 90)/dt.timedelta(minutes = 1)),
     'description' : 'Three months records of information'
     }
    ]

portfolios = [
    {
     'name' : 'Investment Portfolio',
     'description' : 'first portfolio setted into production',
     'client' : 'JuanPChicaC',
     'interval code' : '1m',
     'period code' : '1y'
     },
    {
     'name' : 'Investment Portfolio',
     'description' : 'first portfolio setted into production',
     'client' : 'TestingUser',
     'interval code' : '1m',
     'period code' : '1mo'
     },
#    {
#     'name' : 'Investment Portfolio',
#     'description' : 'Copy of first portfolio that was setted into production',
#     'client' : 'JuanPChicaC',
#     'interval code' : '2m',
#     'period code' : '1mo'
#     },    
    ]




