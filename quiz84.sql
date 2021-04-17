
SELECT FLOOR(2.999) * 
IFNULL(
	COALESCE(
		NULL
		,FLOOR(3)
		,'DailyCoding'
		,FLOOR(1.1)
	)
,1)
	

