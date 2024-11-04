for url in $(cat $1)
do
	gauplus -subs -t 200 $url | sort -u | uniq  > xxe1.txt
	gau --subs --from 200101 --to 202303 --providers wayback,commoncrawl,otx,urlscan --threads 200 $url | sort -u | uniq  >> xxe1.txt
	waybackurls $url | grep $url | sort -u | uniq  >> xxe1.txt
	curl -s "https://urlscan.io/api/v1/search/?q=domain:$url&size=10000" | jq -r '.results[].page.url' | grep $url | sort -u | uniq  >> xxe1.txt
	nodecraw -u https://$url -r -a 50 -t 5 >> xxe1.txt
	cat xxe1.txt| egrep -iv "\.(css|ico|jpg|jpeg|png|bmp|svg|img|gif|mp4|flv|ogv|webm|webp|mov|mp3|m4a|m4p|scss|tif|tiff|ttf|otf|woff|woff2|bmp|ico|eot|htc|rtf|swf|image|exe|js|apng|bpm|png|bmp|gif|heif|ico|cur|jpg|jpeg|jfif|pjp|pjpeg|psd|raw|svg|tif|tiff|webp|xbm|3gp|aac|flac|mpg|mpeg|mp3|mp4|m4a|m4v|m4p|oga|ogg|ogv|mov|wav|webm|eot|woff|woff2|ttf|otf|css)" | sort -u > xxe2.txt
	cat xxe2.txt| grep $url | sed -r 's/https?:\/\///g; s/:[0-9]+//g' | sort -u > xxe3.txt
	httpx -l xxe3.txt -t 2000 | sort -u > xxe4.txt
	nuclei -l xxe4.txt -t xxe.yaml -bs 100 -c 200 -o xxe/xxe-$url.txt
done
