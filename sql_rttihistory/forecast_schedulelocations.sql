SELECT f.*
  FROM Forecasts f
  LEFT JOIN ScheduleLocations sl 
	ON f.ScheduleLocationID = sl.ScheduleLocationId
  WHERE sl.TIPLOC = 10156



  SELECT count ( f.ForecastId), f.ScheduleLocationID, max(sl.TIPLOC) , max(
  FROM [RTTIHistoryECV].[dbo].[Forecasts] f right join ScheduleLocations sl 
	ON f.ScheduleLocationID = sl.ScheduleLocationId
	right join Locations l 
		ON sl.TIPLOC = l.ID
  Group by f.ScheduleLocationID