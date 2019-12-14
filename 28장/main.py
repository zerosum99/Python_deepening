""" 메인 모듈입니다. """

def add(x,y) :
    return x+y

class Python :
    def __init__(self, version) :
        self.version = version
        
    def getVersion(self) :
        return self.version
    

if __name__ == '__main__' :
    print("함수 add  실행 ", add(10,10))
    p = Python('3.7')
    print(" 파이썬 객체 생성", p, p.getVersion())
    
else :
    print("import 처리된 모듈 ")
