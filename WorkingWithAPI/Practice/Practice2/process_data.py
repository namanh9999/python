import get_data

def get_infor(data):
    result = []
    amount_score = []
    plot_dicts = []
    try:
        for value in data:
            score = value['score']
            plot_dict  = {
                'name' : value['by'],
                'type' : value['type'],
            }
            plot_dicts.append(plot_dict)
            amount_score.append(score)
        result.append(amount_score) 
        result.append(plot_dicts)
        return result
    except:
        pass
 