USE RTTIHistoryECV

SELECT   DATEDIFF(minute, f.ArrivalTime, sl.STA) AS ArrivalDelay, 
		DATEDIFF(minute, f.DepartureTime, sl.STD) AS DepartureDelay, 
		l.TIPLOC, l.LocationName,  
		sl.STA, sl.STD,
		r.Code, r.Description AS Reason, 
		f.*
FROM Forecasts f LEFT JOIN Reasons r 
		ON f.LateRunningReasonID = r.Id
	LEFT JOIN ScheduleLocations sl 
		ON f.ScheduleLocationID = sl.ScheduleLocationId
	LEFT JOIN Locations l
		ON sl.TIPLOC = l.ID
WHERE
	f.IsArrivalDelayed =1 OR f.IsDepartureDelayed =1
	
	
	 OR NOT ( f.LateRunningReasonID IS NULL)

