last_sibling=$( curl -XGET localhost:8098/types/default/buckets/test/keys/foo 2>&- | awk 'BEGIN{active=false}/Siblings/{active=true;next}{if( active==true) {print $0;exit} else {}}'  )

echo "Last sibling Vtag is : $last_sibling"
curl -XGET "localhost:8098/types/default/buckets/test/keys/foo?vtag=${last_sibling}"
