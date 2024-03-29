USE RTTIHistoryECV

SELECT COUNT(f.ForecastId) counter, /*(f.LaterunningReasonID, MAX(r.Id),*/ MAX(r.Description) 

FROM Forecasts f LEFT JOIN Reasons r ON f.LateRunningReasonID = r.Id

WHERE
	f.IsArrivalDelayed =1 OR f.IsDepartureDelayed =1 OR NOT ( f.LateRunningReasonID IS NULL)


GROUP BY f.LateRunningReasonID 
GROUP BY DATEPART(hour, f.)
ORDER BY counter DESC

