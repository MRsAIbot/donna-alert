SELECT f.ArrivalTime, f.IsArrivalDelayed, f.DepartureTime, f.IsDepartureDelayed

FROM Forecasts f 

WHERE
	f.IsArrivalDelayed =1 OR f.IsDepartureDelayed =1 OR NOT ( f.LateRunningReasonID IS NULL)





SELECT f.ArrivalTime, f.IsArrivalDelayed, f.DepartureTime, f.IsDepartureDelayed

FROM Forecasts f

WHERE
(	f.IsArrivalDelayed =1 AND f.ArrivalTime IS NULL)

OR

(	f.IsDepartureDelayed =1 AND f.DepartureTime IS NULL)




