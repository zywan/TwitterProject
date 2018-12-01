import mysql.connector


def mysql_statistic(search_key):
	'''
		this part is the statistic analysis of mysql
	'''

	# connect to the mysql
	mydb = mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="12345678",
			database='twitter_mysql'
		)
	mycursor = mydb.cursor()
	search_time = 0
	image_num = 0
	key_list= {}
	sessions = {}
	mycursor.execute("SELECT * FROM activity")
	activity_list = mycursor.fetchall()

	# interate all the data activity table
	for activity in activity_list:
		search_time +=1
		image_num +=int(activity[4])

		if activity[1] not in key_list:
			key_list[activity[1]] = 1
		else:
			key_list[activity[1]] +=1

		if activity[1] == search_key:
			if activity[0] not in sessions:
				sessions[activity[0]] = 1
			else:
				sessions[activity[0]] += 1

	image_per_feed = float(image_num/search_time)
	maximum_search = 0

	print('Overall: ', key_list)
	print('Number of images per feed: ', image_per_feed)
	print('which sessions search',search_key ,": ",sessions)

	for key in key_list:
		maximum_search = max(key_list[key],maximum_search)

	m_pop_twt = []

	for key in key_list:
		if (key_list[key]==maximum_search):
			m_pop_twt.append(key)
			
	print('Most popular: ', m_pop_twt,'searched for: ', maximum_search, 'times')

mysql_statistic('NBAonTNT')

