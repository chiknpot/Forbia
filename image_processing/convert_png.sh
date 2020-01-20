for i in *.jpg ; do
       	convert "$i" "${i%.jpg}.png" 
done
find . -type f -name "*.jpg" -exec rm {} \;	
