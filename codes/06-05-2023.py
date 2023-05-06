def get_distance(name, speed, time_for_speed, time_for_rest, time_for_race):
	runner = {
	    'name': name,
	    'speed': speed,
	    'tfs': time_for_speed,
	    'tfrest': time_for_rest,
	    'tfrace': time_for_race,
	    'dps': speed,
	    'dist': speed * time_for_speed
	}
	up_dist = None
	time_spent, i, distance, state = 0, 1, 0, ''
	while time_spent <= runner['tfrace']:
		if i % 2 == 0:
			state = 'rest'
			time_spent += runner['tfrest']
		else:
			state = 'on the run'
			time_spent += runner['tfs']
			distance += runner['dist']
		i += 1
	if state != 'rest':
		up_dist = distance
		distance -= runner['dist']
		time_spent -= runner['tfs']
		for _ in range(runner['tfs']):
			if time_spent < runner['tfrace']:
				distance += runner['dps']
				time_spent += 1
	return f'distance: {distance}\nstate: {state}\ndistance if on the run: {up_dist}'
	
	
if __name__ == '__main__':
	while True:
		name = input('Name: ')
		speed = int(input('Speed: '))
		time_for_speed = int(input('Time for speed: '))
		time_for_rest = int(input('Time for rest: '))
		time_for_race = int(input('Time for race: '))
		print(get_distance(name, speed, time_for_speed, time_for_rest, time_for_race))