# PetHospital

# Database
使用命令`python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > project_dump.json`可导出整个数据库并且可在服务器上导入