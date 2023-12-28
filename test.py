import fitanalysis

activity = fitanalysis.Activity('testrun.fit')

print(activity.elapsed_time)
print(activity.moving_time)

# Also available for heart rate and cadence
print(activity.mean_power)

print(activity.norm_power)

# Intensity and training stress calculations require
# a functional threshold power value (in Watts)
print(activity.intensity(310))
print(activity.training_stress(310))