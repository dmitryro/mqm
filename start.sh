kill -9 $(pidof uwsgi)
cd /awl/artwell
uwsgi --socket :8001 --module artwell.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:8181 --daemonize=/var/www/vhosts/awlguide.com/logs/uwsg.log
cd /zreal/zrealty 
uwsgi --socket :8005 --module zrealty.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:9191 --daemonize=/var/www/vhosts/zrealtycorp.com/logs/uwsg.logs
cd /ophub/openhub
uwsgi --socket :8010 --module openhub.wsgi --emperor /etc/uwsgi/vassals --uid root --gid root --master --processes 4 --threads 2 --stats 127.0.0.1:9595 --daemonize=/var/www/vhosts/openhub.awlguide.com/logs/uwsg.log
