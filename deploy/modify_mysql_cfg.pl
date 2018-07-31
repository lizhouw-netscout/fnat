#!/usr/bin/perl 

system("cp /etc/mysql/my.cnf /etc/mysql/my.cnf.BAK");
system("rm /etc/mysql/my.cnf");

open(SRC_FILE, "<", "/etc/mysql/my.cnf.BAK");
open(DST_FILE, ">", "/etc/mysql/my.cnf");

while($this_line = <SRC_FILE>){
    if($this_line =~ "^bind-address[ \t]+.*"){
        print DST_FILE "# $this_line";
    }
    else{
        print DST_FILE $this_line;
    }
}

close SRC_FILE;
close DST_FILE;
