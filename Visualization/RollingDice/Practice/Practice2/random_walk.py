from random import choice

def get_step():
    direction = choice([1, -1])
    distance = choice([1,2,3,4,5])
    step = distance * direction
    return step
        
class RandomWalk():
    def __init__(self, number_points=50000):
        self.number_points = number_points
        self.x_value = [0]
        self.y_value = [0]
    

    def  fill_walk(self):
        while len(self.x_value) < self.number_points:
            x_step = get_step()
            y_step = get_step()

            if x_step == 0 and y_step == 0:
                continue
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)