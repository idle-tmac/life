ps aux |grep manage.py  |grep -v grep  |awk  '{print $2}' | while read d;do kill -9 $d;done
nohup python manage.py runserver 0:8081 >log 2>err &
