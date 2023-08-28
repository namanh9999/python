import get_data 
import process_data
import visual_data
path= "DataVisualization/WorkingWithAPI/Practice/Practice2/data.json" 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json' 
# data = get_data.load_data(path, url)
data = get_data.only_load(path)
data1 = process_data.get_infor(data)
print(data1)
visual_data.visual_pygal(data1)
