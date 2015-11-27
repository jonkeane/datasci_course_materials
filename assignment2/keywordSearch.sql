SELECT max(sim) FROM (
	SELECT docid, sum(prod) as sim FROM (
	SELECT
	*,
	docs.docid as row,
	keywords.docid as col,
	-- A.count,
	-- B.count,
	docs.count *	keywords.count as prod
	FROM
	(SELECT * FROM frequency)docs,
	(SELECT 'q' as docid, 'washington' as term, 1 as count
	UNION
	SELECT 'q' as docid, 'taxes' as term, 1 as count
	UNION
	SELECT 'q' as docid, 'treasury' as term, 1 as count)keywords
WHERE docs.term = keywords.term
) GROUP BY row,col
)
;
