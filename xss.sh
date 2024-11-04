for i in `cat $1`;do
   python3 ~/Tools/ParamSpider/paramspider.py -d  $i --exclude woff,css,js,png,svg,jpg
done;
cd output
cat *.* txt | kxss |tee  kxss.txt
