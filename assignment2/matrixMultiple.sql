SELECT res FROM (
SELECT row, col, sum(prod) as res FROM (
	SELECT
	*,
 	A.row_num as row,
	B.col_num as col,
	-- A.value,
	-- B.value,
	A.value *	B.value as prod
	FROM A, B
	WHERE A.col_num = B.row_num
) GROUP BY row, col
) WHERE row = 2 AND col = 3
;
