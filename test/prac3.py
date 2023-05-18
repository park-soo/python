rides = '''와일드 윙: 110cm 이상
드림보트: 120cm 이상
자이안트 루프: 120cm 이상
툼 오브 호러: -
플라이벤처: 140cm~195cm
회전목마: 100cm 이상
매직 붕붕카: 110cm~140cm'''

def read(text):
    ridename,limit = map(str.strip,text.split(':'))
    
    cmmin=cmmax=None
    if '~' in limit:
        temp=[]
        for t in limit.split('~'):
            temp.append(t.replace('cm',''))
        cmmin,cmmax=int(temp[0]),int(temp[1])
    elif '이상' in limit:
        cmmin=int(limit.split("cm")[0])
    return ridename,cmmin,cmmax
    

def allowedrides(height):
    result = [] 
    for ride in rides.splitlines():
        ridename, cmmin, cmmax = read(ride)
        if (not cmmin and not cmmax) or (height >= cmmin and not cmmax) or (cmmin <= height <= cmmax):
            result.append(ridename)
    
    return result


if __name__ == "__main__":
    height = int(input())
    for answer in allowedrides(height):
        print(answer)