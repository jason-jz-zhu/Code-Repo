/*
Enter your query here.
*/
select '2&3&5&7&11&13&17&19&23&29&31&37&41&43&47&53&59&61&67&71&73&79&83&89&97&101&103&107&109&113&127&131&137&139&149&151&157&163&167&173&179&181&191&193&197&199&211&223&227&229&233&239&241&251&257&263&269&271&277&281&283&293&307&311&313&317&331&337&347&349&353&359&367&373&379&383&389&397&401&409&419&421&431&433&439&443&449&457&461&463&467&479&487&491&499&503&509&521&523&541&547&557&563&569&571&577&587&593&599&601&607&613&617&619&631&641&643&647&653&659&661&673&677&683&691&701&709&719&727&733&739&743&751&757&761&769&773&787&797&809&811&821&823&827&829&839&853&857&859&863&877&881&883&887&907&911&919&929&937&941&947&953&967&971&977&983&991&997';



SELECT
	FinalResults.OriginalNumber
FROM
(
	SELECT
		DivResults.OriginalNumber,
		COUNT(*)
	FROM
	(
		SELECT
			Sequence.x AS OriginalNumber,
			Sequence.x % NumberGenerator2.x AS DivMod
		FROM
		(
			SELECT
				NumberGenerator.x
			FROM
			(
				-- Since MySQL doesn't have a number/sequence generator like other DBMS's,
				-- I'm using this one that @RolandoMySQLDBA answered in this question:
				-- http://dba.stackexchange.com/questions/75785/how-to-generate-a-sequence-in-mysql
				-- This will generate a sequence from 1 to 1000.
				SELECT
					(h*100+t*10+u+1) x
				FROM
			 	(
			 		SELECT 0 h
		 			UNION SELECT 1
	 				UNION SELECT 2
	 				UNION SELECT 3
	 				UNION SELECT 4
	 				UNION SELECT 5
	 				UNION SELECT 6
	 				UNION SELECT 7
	 				UNION SELECT 8
	 				UNION SELECT 9
 				) A,
			 	(
			 		SELECT 0 t
			 		UNION SELECT 1
			 		UNION SELECT 2
			 		UNION SELECT 3
			 		UNION SELECT 4
			 		UNION SELECT 5
			 		UNION SELECT 6
			 		UNION SELECT 7
			 		UNION SELECT 8
			 		UNION SELECT 9
		 		) B,
			 	(
			 		SELECT 0 u
			 		UNION SELECT 1
			 		UNION SELECT 2
			 		UNION SELECT 3
			 		UNION SELECT 4
			 		UNION SELECT 5
			 		UNION SELECT 6
			 		UNION SELECT 7
			 		UNION SELECT 8
			 		UNION SELECT 9
		 		) C
			) AS NumberGenerator
			WHERE
				x > 1
			ORDER BY
				x
		) AS Sequence,
		(
			SELECT
				(h*100+t*10+u+1) x
			FROM
		 	(
		 		SELECT 0 h
	 			UNION SELECT 1
 				UNION SELECT 2
 				UNION SELECT 3
 				UNION SELECT 4
 				UNION SELECT 5
 				UNION SELECT 6
 				UNION SELECT 7
 				UNION SELECT 8
 				UNION SELECT 9
			) A,
		 	(
		 		SELECT 0 t
		 		UNION SELECT 1
		 		UNION SELECT 2
		 		UNION SELECT 3
		 		UNION SELECT 4
		 		UNION SELECT 5
		 		UNION SELECT 6
		 		UNION SELECT 7
		 		UNION SELECT 8
		 		UNION SELECT 9
	 		) B,
		 	(
		 		SELECT 0 u
		 		UNION SELECT 1
		 		UNION SELECT 2
		 		UNION SELECT 3
		 		UNION SELECT 4
		 		UNION SELECT 5
		 		UNION SELECT 6
		 		UNION SELECT 7
		 		UNION SELECT 8
		 		UNION SELECT 9
	 		) C
		) AS NumberGenerator2
		WHERE
			-- We just need to check numbers that are <= square root of the original number to be tested
			NumberGenerator2.x <= FLOOR(SQRT(Sequence.x))
		ORDER BY
			Sequence.x, NumberGenerator2.x
	) AS DivResults
	WHERE
		DivResults.DivMod = 0
	GROUP BY
		DivResults.OriginalNumber
	HAVING
		COUNT(*) = 1
) AS FinalResults
