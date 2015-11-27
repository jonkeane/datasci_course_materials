SELECT sum(prod) FROM (
	SELECT
	*,
	A.docid as row,
	B.docid as col,
	A.count,
	B.count,
	A.count *	B.count as prod
	FROM
	(SELECT * FROM frequency
	WHERE docid = "10080_txt_crude")A,
	(SELECT * FROM frequency
	WHERE docid = "17035_txt_earn")B
WHERE A.term = B.term
) GROUP BY row,col;
