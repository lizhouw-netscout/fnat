#!/bin/bash
#
#         fnat_webportal_deploy.sh (Copyright reserved Eleborate 2015)
#
#  This script is used to deploy test server components of FNAT system. To run it, you
#  must keep the structure of original eleborate release package.
#  Please contact Eleborate at eleborate@hotmail.com to get support.
#--------------------------------------------------------------------------------------
# Feb. 19. 2015.  |  This first draft of script.

PACKAGE_ROOT=`dirname $0`/../
if [ `whoami` != "root" ];
then
	echo "The script can be run with root privilege only."
	exit -1
fi

dist_id=`cat /etc/lsb-release | grep DISTRIB_ID | awk -F= '{print $2}'`
if [ $dist_id != "Ubuntu" ];
then
	echo "FNAT web portal auto-deployment supports Ubuntu only."
	exit -2
fi

echo "Start to deploy FNAT web portal system..."

echo "Install system dependencies..."
apt-get -y install apache2 
apt-get -y install php5 
apt-get -y install libapache2-mod-php5 
apt-get -y install mysql-server 
apt-get -y install mysql-client 
apt-get -y install python-mysqldb 
apt-get -y install php5-mysql
apt-get -y install nfs-kernel-server
echo "/var/www/html/fnat_log  *(rw,sync,no_root_squash)" >> /etc/exports
service rpcbind restart
service nfs-kernel-server restart

echo "Configure apache server..."
cp ${PACKAGE_ROOT}/deploy/www/* /var/www/html/
cp -R ${PACKAGE_ROOT}/deploy/www/Classes /var/www/html
cp ${PACKAGE_ROOT}/deploy/www/icons/cust-logo.png /usr/share/apache2/icons/
rm -f /var/www/html/index.html
mkdir /var/www/html/fnat_log
mkdir /var/www/html/fnat_log/reports
chmod 777 /var/www/html/fnat_log
chmod 777 /var/www/html/fnat_log/reports
service apache2 restart

mkdir /var/fnat
cp FNAT_report_template.xlsx /var/fnat/FNAT_report_template.xlsx
cp clr_obsolete_report.sh /var/fnat/clr_obsolete_report.sh
chmod +x /var/fnat/clr_obsolete_report.sh
echo "0 10    * * *   root    /var/fnat/clr_obsolete_report.sh /var/www/html/fnat_log/reports 14" >> /etc/crontab
service cron restart
perl ./modify_mysql_cfg.pl

echo ""
echo "Success"
echo "=======================  NOTICE  ================================"
echo "Please run command 'mysql -u root -p' to activate mysql client"
echo "and run 'source $1/create_fnat_database.sql' to create FNAT database."
echo "After that, the FNAT system is deployed successfully."



