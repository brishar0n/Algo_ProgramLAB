class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    def set_x(self,x):
        self.__x = x
    def set_y(self,y):
        self.__y = y

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    
p=Point(1,2)

def get_json_str(other):
    return {"__class__": "Point","x": other.get_x(),"y": other.get_y()}

def read_json_str(s):
    p = Point(int(s),0)
    return get_json_str(p)

z=(get_json_str(p))
print(z)

b = read_json_str("9")
print(b)