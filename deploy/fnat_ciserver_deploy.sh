#!/bin/bash

if [ `whoami` != "root" ];
then
        echo "The script can be run with root privilege only."
        exit -1
fi

dist_id=`cat /etc/lsb-release | grep DISTRIB_ID | awk -F= '{print $2}'`
if [ $dist_id != "Ubuntu" ];
then
        echo "FNAT CI system auto deplaoyment supports Ubuntu only."
        exit -2
fi

wget -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key add -
apt-add-repository -y "deb http://pkg.jenkins-ci.org/debian binary/"

apt-get update
apt-get -y install jenkins

echo Success.
