#!/bin/bash
#
#         fnat_testserver_deploy.sh (Copyright reserved Eleborate 2015)
#
#  This script is used to deploy test server components of FNAT system. To run it, you
#  must keep the structure of original eleborate release package.
#  Please contact Eleborate at eleborate@hotmail.com to get support.
#--------------------------------------------------------------------------------------
# Feb. 18. 2015.  |  This first draft of script.

if [ `whoami` != "root" ];
then
	echo "The script can be run with root privilege only."
	exit -1
fi

dist_id=`cat /etc/lsb-release | grep DISTRIB_ID | awk -F= '{print $2}'`
dist_ver=`cat /etc/lsb-release | grep DISTRIB_RELEASE | awk -F= '{print $2}'`
if [[ $dist_id != "Ubuntu" ]] && [[ $dist_ver != "14.04" ]];
then
	echo "FNAT Test Server auto deployment supports Ubuntu 14.04 only."
	exit -2
fi

echo "Start to deploy FNAT Test Server..."

echo "Install system dependencies..."
apt-get -y install python-pip python-nose python-opencv
pip install uiautomator
pip install nose-testconfig
pip install selenium
pip install pymongo

mkdir /var/fnat
mkdir /var/fnat/fnat_log
chmod 777 /var/fnat/fnat_log
cp ../fnat_rdser/fnat_rdser /var/fnat 

echo Success
