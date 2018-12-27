#encoding:utf-8
import os
import sys
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
#from common.decorator import super_admin_required
#from common.decorator import common_admin_required
#from common.sendmail import SendEmail
#from common.basic_tool import download_files
#from common.util import newServerXlsxByLocalXlsx
#from common.exldeal import XLSDeal
#from server_conf import *
#from admin.project_admin import PojectAdminitor
#from admin.version_admin import VersionAdminitor
#from admin.temp_data_admin import TempDataAdminitor
#from dm.dm_engine import DmEngine
#from dm.online_server import OnlineServer
from model.t_job import JobModel
#from cyberin_iter.master import AutoCyberinIter 
from datetime import datetime, date, timedelta
import json
import logging
import traceback

g_project_path = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件夹的路径
log_error = logging.getLogger('error')
log_machiner = logging.getLogger('debug')


def index(request):
    city = request.GET.get('city', '北京')
    job_direction = request.GET.get('job_direction', '1')
    days_15 = (date.today() + timedelta(days=-15)).strftime("%Y-%m-%d")
    #city = "北京"
    #job_direction = "1"
    jobinfo = JobModel().getJobInfoForWebPage(city = city, job_direction = job_direction, publish_time = days_15)
    d_job = {'city' : city, 'job_direction': str(job_direction), 'jobinfo' : jobinfo}
    return render(request, 'index.html', d_job)

def chat(request):
    return render(request, 'chat.htm')
