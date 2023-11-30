def pulse(training_type, age):
    max_heart_rate = 220 - age
    
    if training_type == 'fitness':
        min_heart_rate_range = round(max_heart_rate * 0.6)
        max_heart_rate_range = round(max_heart_rate * 0.7)
        heart_rate_range = (min_heart_rate_range, max_heart_rate_range)
    
    elif training_type == 'aerobic':
        min_heart_rate_range = round(max_heart_rate * 0.7)
        max_heart_rate_range = round(max_heart_rate * 0.8)
        heart_rate_range = (min_heart_rate_range, max_heart_rate_range)
    
    elif training_type == 'anaerobic':
        min_heart_rate_range = round(max_heart_rate * 0.8)
        max_heart_rate_range = round(max_heart_rate * 0.9)
        heart_rate_range = (min_heart_rate_range, max_heart_rate_range)
    
    else:
        print ('There is no such type of training in the database')
        quit()
    
    return heart_rate_range

training = input ('Enter the type of training: ').lower().strip()
user_age = int (input('Enter your age '))

user_pulse = pulse(training, user_age)

print ('Your heart rate zone should be between', user_pulse[0], 'and', user_pulse[1], 'bpm')