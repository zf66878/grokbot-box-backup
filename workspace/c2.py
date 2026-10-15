import paramiko
k=paramiko.Ed25519Key.from_private_key_file('/home/box/.ssh/id_ed25519')
J={('root','42.121.223.54'):"cd /root/qiji/logs;for f in payroll_monthly fengong_kaoping fengong_remind team_task_dd xgj baoming_push daily_breakeven;do echo \"## $f $(stat -c %y $f.log|cut -c1-16)\";tail -4 $f.log|cut -c1-200;done;grep -l '7411\\|7413' *.log;grep -h '超过限制' *.log|tail -1|cut -c1-60;ls /root/qiji_payroll|head -30;systemctl status certbot --no-pager|tail -3;docker ps -a|grep -i chev",
('root','121.43.49.208'):"tail -5 /www/wwwlogs/www.qiji.com.cn.error.log|cut -c1-200;last -x|head -4",
('root','173.242.117.211'):"cd /var/log/notion-sync;ls -t|head -5;grep -liE 'error|traceback' $(ls -t|head -15) ;tail -3 health.log system_audit.log|cut -c1-200;docker logs --tail 3 claude-event-runner 2>&1|cut -c1-200"}
for (u,h),cmd in J.items():
  print('=====',h);c=paramiko.SSHClient();c.set_missing_host_key_policy(paramiko.AutoAddPolicy());c.connect(h,username=u,pkey=k,timeout=15)
  _,o,e=c.exec_command(cmd,timeout=60);print(o.read().decode(errors='replace')[:5000],e.read().decode(errors='replace')[-300:])
