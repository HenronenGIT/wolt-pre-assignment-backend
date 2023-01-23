from utils.helpers import *

def test_rush_hour():
	rush_hours = [
		"2023-1-20T15:00:00Z",
		"2023-1-20T16:00:00Z",
		"2023-1-20T19:00:00Z"
		]

	for time in rush_hours:
		assert rush_hour(time) == True

def test_not_rush_hour():
	not_rush_hours = [
		"2023-1-20T14:00:00Z",
		"2023-1-20T20:00:00Z",
		"2023-1-19T19:00:00Z"
		]
	
	for time in not_rush_hours:
		assert rush_hour(time) == False
