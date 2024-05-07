import pandas as pd

def NM_encode(inp:int):
    in_num=str(inp)
    result:str=""
    while True:
        if len(in_num)>=3:
            inm=int(in_num[0:3])
            result+=format(inm,'010b')
            in_num=in_num[3:]
        elif len(in_num)==2:
            inm=int(in_num[0:2])
            result+=format(inm,'07b')
            break
        elif len(in_num)==1:
            inm=int(in_num[0])
            result+=format(inm,'04b')
            break
        if len(in_num)<=0:
            break
    return result
def AL_encode():
     
if __name__=="__main__":
    p=NM_encode(9876)
    print(p)