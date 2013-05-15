INPUT=`dirname $0`/json/example.json
JOBID=`sparqueue-cli submit $INPUT`
while [ "$STATUS" != "SUCCESS" -a "$STATUS" != "FAILED" ]
do
	STATUS=`sparqueue-cli status -text $JOBID`
	echo "$JOBID=$STATUS"
    sleep 1
done

sparqueue-cli job $JOBID

echo "$JOBID finished with status $STATUS"