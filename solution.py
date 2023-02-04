class FactorHandler:
    def __init__(self):
        self.factor_list = [] 
    def sort_func(self , time_format , time) :
        data = [time_format , time]
        get = data[0][:1]
        if get == 'y' : 
            get = data[0][6:7]
            if get == 'd' : 
                data[1] = f"{data[1][:4]}/{data[1][8:]}/{data[1][5:7]}"
        elif get == 'm' :
            get = data[0][3:4]
            if get == 'y' : data[1] = f"{data[1][3:7]}/{data[1][:2]}/{data[1][8:]}" 
            else : data[1] = f"{data[1][6:]}/{data[1][:2]}/{data[1][3:5]}" 
        else :
            get = data[0][3:4]
            if get == 'y' : data[1] = f"{data[1][3:7]}/{data[1][8:]}/{data[1][0:2]}" 
            else : data[1] = f"{data[1][6:]}/{data[1][3:5]}/{data[1][0:2]}"
        data[0] = 'yyyy' + '/' + 'mm' + '/' + 'dd'
        return data

    def add_factor(self, time_format, time, value):
        data = self.sort_func(time_format , time)
        data.append(value)
        self.factor_list.append(data)
        self.factor_list.sort(key=lambda date : date[1])
        
        
    def remove_all_factors(self, time_format, time):
        data = self.sort_func(time_format , time)
        indexs = []
        for num in range(len(self.factor_list)) : 
            if self.factor_list[num][1] == data[1] : indexs.append(num)
        count = 0
        for num in indexs : 
            self.factor_list.pop(num - count)
            count += 1
    
    def get_sum(self, time_format, start_time, finish_time):
        if len(self.factor_list) == 0 : return 0 
        input_time1 = self.sort_func(time_format , start_time)
        input_time2 = self.sort_func(time_format , finish_time)
        sum = 0
        for date in range(len(self.factor_list)) :
            if input_time1[1] <= self.factor_list[date][1] <= input_time2[1] : sum += self.factor_list[date][2]
        return sum