WITH lat AS (

   SELECT lat, uf FROM   

   (SELECT 
		[AC],[AL],[AM],[AP],[BA],[CE],[DF],[ES],[GO],[MA],[MT],[MS],[MG],
		[PA],[PB],[PR],[PE],[PI],[RJ],[RN],[RO],[RS],[RR],[SC],[SE],[SP],[TO]
  
	FROM [B3_DATA_DISCOVERING].[dbo].[latitude_estados]) p  

	UNPIVOT  

   (
	   lat FOR uf IN   
	   ([AC],[AL],[AM],[AP],[BA],[CE],[DF],[ES],[GO],[MA],[MT],[MS],[MG],
	   [PA],[PB],[PR],[PE],[PI],[RJ],[RN],[RO],[RS],[RR],[SC],[SE],[SP],[TO]
	)
)AS unpvt

),

long AS (


   SELECT long, uf  FROM   
   (SELECT 
		[AC],[AL],[AM],[AP],[BA],[CE],[DF],[ES],[GO],[MA],[MT],[MS],[MG],
		[PA],[PB],[PR],[PE],[PI],[RJ],[RN],[RO],[RS],[RR],[SC],[SE],[SP],[TO]
  
	FROM [B3_DATA_DISCOVERING].[dbo].[longitude_estados]) p  
	
	UNPIVOT  

   (
   long FOR uf IN   
   ([AC],[AL],[AM],[AP],[BA],[CE],[DF],[ES],[GO],[MA],[MT],[MS],[MG],
   [PA],[PB],[PR],[PE],[PI],[RJ],[RN],[RO],[RS],[RR],[SC],[SE],[SP],[TO]
   )
	
	)AS unpvt2
	)

			SELECT 
			lat.uf,
			lat.lat,
			long.long
			FROM lat
			LEFT JOIN long on lat.uf = long.uf


