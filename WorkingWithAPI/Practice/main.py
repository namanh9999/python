import data_process 
import visual_data
import get_and_dump as GAD

relative_path = "DataVisualization/WorkingWithAPI/Practice/data.json"
url = 'http://api.github.com/search/repositories?q=language:java&sort=stars'

GAD.get_and_dump(relative_path,url)
data = GAD.load_data(relative_path)
final_result = data_process.get_infor(data)
# visual_data.visual_chart(final_result)
visual_data.visual_plot(final_result)
data_and_description = data_process.get_data_description(data)
visual_data.visual_chart(data_and_description)