# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 用户表
class User(models.Model):
	code = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	pwd = models.CharField(max_length=20)