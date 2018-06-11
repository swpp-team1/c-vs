echo '------ Initialization start! ------'
echo '------ Delete BD and re-create ----'
rm -f db.sqlite3
rm -r cvs_rest/migrations/
python manage.py makemigrations cvs_rest
python manage.py migrate
echo '------ Creating users start! ------'
python manage.py shell < inittest.py
echo '------ Creating user finish! ------'
echo '------ Create products start! -----'
python ./crawlers/gs25_parser.py
python ./crawlers/cu_parser.py
python ./crawlers/seveneleven_parser.py > ./crawlers/SE.dic
python ./crawlers/register.py ./crawlers/SE.dic SE
echo '------ Create products finish! ----'
echo '------ Initialization finish! -----'
