# How many seconds are there in 42 minutes and 42 seconds?

def secondsInMinutes():
    minutes = 42
    seconds = 42
    totalSeconds = (minutes * 60) + seconds
    return totalSeconds

def milesInKilometres():
    kilometres = 10
    mileRatio = 1.61
    totalMiles = kilometres/mileRatio
    return totalMiles

def secondsToMinutes(seconds):
    minutes = seconds / 60
    seconds = seconds % 60

    return int(minutes), int(seconds)


def raceCalculation():

    totalMiles = milesInKilometres()
    totalSeconds = secondsInMinutes()

    SecondsPerMile = totalSeconds/totalMiles

    return SecondsPerMile


raceTime = raceCalculation()
raceMinutes, raceSeconds = secondsToMinutes(raceTime)

print(raceMinutes, raceSeconds)