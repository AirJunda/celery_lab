
## celery 相关命令
* celery -A celery_app worker -l INFO
* celery -A celery_app beat -l INFO

## git 相关
```shell
# push local init commit to master rather than main 
git push -u origin master

# create and switch to new branch locally
git branch django_lab
git checkout django_lab

# django 
django-admin startproject imooc
cd imooc
```

## django项目中使用 celery worker
```shell
cd imooc
celery -A course worker -l INFO
celery -A course beat -l INFO
```


## flower监控的使用
```shell
pip install flower
celery --broker='redis://192.168.1.42:6379' flower

```
