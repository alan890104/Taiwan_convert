import fiona
from shapely.geometry import shape, Point
import os


townnames = {}

def names():
    
    dir = os.path.dirname(__file__)
    taiwan = fiona.open(os.path.join(dir, 'TOWN_MOI_1090324.shp')) #shp、dbf、shx 檔案要放在目錄下
    
    f = open("dict.txt","w")
    for township in taiwan:
        town_id = township['properties']['TOWNCODE']  #鄉鎮代碼
        townnames[town_id] =  township['properties']['TOWNNAME'] + ', ' + township['properties']['COUNTYNAME']
        f.write(townnames[town_id]+'\n')
    f.close()



if __name__ == '__main__':
    names()
