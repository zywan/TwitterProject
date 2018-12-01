import pymongo
from random import choice
id_pool = ['NBA','lol','kobe','james','SLAMonline','NBAonTNT','StephenCurry30','JHarden13','JLin7','HoustonRockets']
def mongo_statistic(search_key):
	client = pymongo.MongoClient()
	mydb = client["twitter_mongo"]
	mycol = mydb["user"]
	search_time = 0
	image_num = 0
	key_list = {}
	sessions = {}
	for record in mycol.find():
		search_time += 1
		image_num += len(record['url_list'])
		if record['searchID'] not in key_list:
			key_list[record['searchID']] = 1
		else:
			key_list[record['searchID']] +=1
			
		if record['searchID'] == search_key:
			# sessions.append(record['username'])
			if record['username'] in sessions:
				sessions[record['username']] += 1
			else:
				sessions[record['username']] = 1

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

# id = choice(id_pool)
mongo_statistic('NBAonTNT')


