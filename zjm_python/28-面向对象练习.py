class House(object):
    def __init__(self, house_type, total_area, fru_list=None):
        if fru_list is None:  # 如果这个值是None
            fru_list = []  # 将fru_list设置为空列表
        self.house_type = house_type
        self.total_area = total_area
        self.free_area = total_area * 0.6
        self.fru_list = fru_list

    def add_fru(self, x):
        if self.free_area < x.area:
            print('剩余空间不足')
        else:
            self.fru_list.append(x.name)
            self.free_area -= x.area

    def __str__(self):
        return '户型={},总面积={},剩余面积={},家具列表={}'.format(self.house_type, self.total_area, self.free_area, self.fru_list)


class Furniture(object):
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象的时候，传如户型和总面积
house = House('两室一厅', 20)

sofa = Furniture('沙发', 10)
bed = Furniture('席梦思', 4)
chest = Furniture('衣柜', 2)
table = Furniture('餐桌', 1.5)

house.add_fru(sofa)
house.add_fru(bed)
house.add_fru(chest)
house.add_fru(table)


print(house)
