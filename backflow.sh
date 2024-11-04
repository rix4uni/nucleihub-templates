#!/bin/bash
ok="\033[32m[+]\033[0m"
no="\033[31m[+]\033[0m"
clear
function logo(){
  echo -e """

  \033[31m█▄▄ ▄▀█ █▀▀ █▄▀ ▄▄ █▀▀ █░░ █▀█ █░█░█\033[0m
  \033[31m█▄█ █▀█ █▄▄ █░█ ░░ █▀░ █▄▄ █▄█ ▀▄▀▄▀\033[0m
  ===================================
  Web-App Testing Suite\033[31m[SYSTEM00 SECURITY]\033[0m
  ===================================

  """
}
function takeover_scan(){
    echo -e "$ok Detecting Possible Subdomain takeover of $(cat $1 |wc -l ) Subdomains wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
    nuclei -silent -l $1 -t takeovers/ -o takeover.result
}
function open_redirect(){
    echo -e "$ok Scanning for open redirect wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
    nuclei -silent -l $1 -t vulnerabilities/generic/open-redirect.yaml -o redirect.result
}
function phpmyadmin(){
  echo -e "$ok Scanning for Php My admin Setup page wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
  nuclei -silent -l $1 -t miscellaneous/phpmyadmin-setup.yaml -o phpmyadminsetup.result
}
function tech_detect(){
  echo -e "$ok Detecting Technologies of $(cat $1 |wc -l ) Subdomains wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
  nuclei -silent -l $1 -t technologies/ -o detection.txt
}
function network_flaw(){
  echo -e "$ok Scanning for Network Flaw wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
  nuclei -silent -l $1 -t network/ -o network.result
}
function wordpress_workflow(){
echo -e "$ok Filtering Wordpress Sites"
cat detection.txt | grep "wordpress" | clean url | tee wordpress.sites
echo -e "$ok Testing $(cat wordpress.sites|wc -l) Wordpress Site wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
nuclei -silent -l wordpress.sites -t templates/wordpress/ -o wordpress.result
}
function bigip_workflow(){
  cat detection.txt | grep "bigip" | clean url | tee bigip.sites
  echo -e "$ok Testing $(cat bigip.sites|wc -l) Bigip Site wait or $(curl -s https://www.boredapi.com/api/activity | jq .activity)"
  nuclei -silent -l bigip.sites -t cves/2020/CVE-2020-5902.yaml -o bigip.result
}

logo
takeover_scan $1
open_redirect $1
phpmyadmin $1
tech_detect $1
wordpress_workflow
bigip_workflow
