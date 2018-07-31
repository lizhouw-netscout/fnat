#!/bin/bash 

# The syntax:
# clr_obsolete_report.sh  target_directory  obsolate_threshold
target_directory=${1}
epoch_span=$((${2}*24*60*60))
current_epoch=`date +%s`
for report in ${target_directory}/*.xlsx;
do
	its_epoch=`stat -c %Y ${report}`
	its_epoch=$((${current_epoch}-${its_epoch}))
	if [ ${its_epoch} -gt ${epoch_span} ];
	then
		rm -rf ${report}
	fi
done
