# How many seconds are there in 42 minutes and 42 seconds?
def secondsInMinutes():
    minutes = 42
    seconds = 42
    totalSeconds = (minutes * 60) + seconds
    return totalSeconds

# How many miles are there in 10 kilometres?
def milesInKilometres():
    kilometres = 10
    mileRatio = 1.61
    totalMiles = kilometres/mileRatio
    return totalMiles

# Convert seconds to minutes and seconds
def secondsToMinutes(seconds):
    minutes = seconds / 60
    seconds = seconds % 60
    return int(minutes), int(seconds)

# Calculate the pace (Time per mile)
def calculatePace():
    totalMiles = milesInKilometres()
    totalSeconds = secondsInMinutes()
    SecondsPerMile = totalSeconds/totalMiles
    return SecondsPerMile

# Calculate the average speed (miles per second)
def calculateAverageSpeed():
    totalMiles = milesInKilometres()
    totalSeconds = secondsInMinutes()
    milesPerSecond = totalMiles/totalSeconds
    return milesPerSecond


# Calculate pace
pace = calculatePace()
raceMinutes, raceSeconds = secondsToMinutes(pace)
print(raceMinutes, raceSeconds)

# Calculate average miles per second and convert it to miles per hour
averageMph = 3600/pace
print(averageMph)
