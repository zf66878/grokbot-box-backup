import paramiko,sys
hosts={'a2':('root','121.43.49.208'),'a1':('root','42.121.223.54'),'bwg':('root','173.242.117.211'),'tx':('ubuntu','42.192.108.235')}
common="hostname;uptime;df -h / | tail -1;free -m|sed -n 2p;docker ps -a --format '{{.Names}} {{.Status}}' 2>/dev/null;crontab -l 2>/dev/null|grep -v '^#';ls /etc/cron.d;systemctl list-units --type=service --state=running --no-legend 2>/dev/null|awk '{print $1}'|grep -vE 'systemd|dbus|getty|ssh|cron|rsyslog|polkit|udev|chrony|network|snap|multipath|unattended|irqbalance|accounts|atd|tuned|auditd|aliyun|qemu|serial|user@|logind|journal'; systemctl --failed --no-legend"
extra={'a2':"ss -ltnp|awk '{print $4,$6}'|grep -E ':(80|443|3306|8888) ';ps aux|grep -E '[m]ysqld|[m]ariadb'|awk '{print $11}'|head -3;nginx -t 2>&1||/www/server/nginx/sbin/nginx -t 2>&1;echo|openssl s_client -connect qiji.com.cn:443 -servername qiji.com.cn 2>/dev/null|openssl x509 -noout -dates -subject;echo|openssl s_client -connect www.qiji.com.cn:443 -servername www.qiji.com.cn 2>/dev/null|openssl x509 -noout -enddate;for f in /www/server/panel/vhost/cert/*/fullchain.pem;do echo $f;openssl x509 -in $f -noout -enddate;done;curl -sk -o /dev/null -w 'http %{http_code}\n' https://qiji.com.cn;curl -s -o /dev/null -w 'http80 %{http_code}\n' http://qiji.com.cn;tail -5 /www/server/data/*.err 2>/dev/null|cut -c1-200;ls /www/wwwlogs/*error* 2>/dev/null|head;tail -3 /www/wwwlogs/qiji*error*.log 2>/dev/null|cut -c1-200",
'a1':"ls ~/qiji_payroll_dws;ls -lt ~/qiji_payroll_dws/logs 2>/dev/null|head -5;f=$(ls -t ~/qiji_payroll_dws/logs/* 2>/dev/null|head -1);[ -n \"$f\" ]&&tail -15 $f|cut -c1-220;ls -lt ~/qiji_payroll_dws/data 2>/dev/null|head -8;grep -rhoiE '(errcode.{0,40}|88.{0,3}|limit.{0,60}|quota.{0,60}|超.{0,30})' --include=*.log ~ 2>/dev/null|sort|uniq -c|sort -rn|head -8;ss -ltnp|awk '{print $4,$6}'|head -20",
'bwg':"ss -ltnp|awk '{print $4,$6}'|head;ss -lunp|awk '{print $4,$6}'|head",
'tx':"docker logs --since 2h $(docker ps -q|head -1) 2>&1|tail -5|cut -c1-200"}
k=paramiko.Ed25519Key.from_private_key_file('/home/box/.ssh/id_ed25519')
for n,(u,h) in hosts.items():
  print('=====',n,h)
  try:
    c=paramiko.SSHClient();c.set_missing_host_key_policy(paramiko.AutoAddPolicy());c.connect(h,username=u,pkey=k,timeout=15)
    _,o,e=c.exec_command(common+';echo ---;'+extra[n],timeout=90);print(o.read().decode(errors='replace')[:6000]);print(e.read().decode(errors='replace')[-800:])
  except Exception as x: print('ERR',x)
