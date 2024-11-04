#!/bin/bash

domain=$1

echo -e "\e[32m-----------------------------------------------\e[0m"
echo -e "\e[32m Starting AssetFinder\e[0m"
echo -e "\e[32m-----------------------------------------------\e[0m"
assetfinder --subs-only $1 | sort -u >$1.txt

echo -e "\e[32m-----------------------------------------------\e[0m"
echo -e "\e[32m Starting Subfinder\e[0m"
echo -e "\e[32m-----------------------------------------------\e[0m"
subfinder -d $1 | sort -u >>$1.txt

export CHAOS_KEY=< Api_Key >

echo -e "\e[32m-----------------------------------------------\e[0m"
echo -e "\e[32m Starting Chaos\e[0m"
echo -e "\e[32m-----------------------------------------------\e[0m"
chaos -d $1 | sort -u >>$1.txt
