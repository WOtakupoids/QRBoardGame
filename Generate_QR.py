from pprint import pprint
import re
import numpy as np
from QR_parameter import Generate_parameter
import pandas as pd
import os
class QR():
    def __init__(self,QR_parm:Generate_parameter) -> None:
        self.matrix=QR_parm.matrix
        self.QR_list=np.zeros((self.matrix,self.matrix))
        self.pram=QR_parm
    def generate_QR(self):
        return
    def validate_inp(self,inp):
        am = re.compile('[a-zA-Z]+')
        nm = re.compile('[0-9]+')
        mode:int=0b0001
        if nm.fullmatch(inp):
            mode=0b0001
        elif am.fullmatch(inp):
            mode=0b0010
        else:
            mode=0b0100
        v_table=pd.read_csv('version_table.csv')
        v_table[]
    def add_symbol(self):
        symbol=np.ones((7,7))
        symbol[1:6,1:6]=0
        symbol[2:5,2:5]=1
        self.QR_list[0:7,0:7]=symbol
        self.QR_list[0:7,-7:]=symbol
        self.QR_list[-7:,0:7]=symbol
        
    def get_tui_QR(self):
        l1=""
        for i in self.QR_list:
            for j in i:
                if j==0:
                    l1+="  "
                else:
                    l1+="■ "
            l1+="\n"
        return l1
if __name__=="__main__":
    Qp=Generate_parameter("a")
    Qp.versinon=1
    qr=QR(Qp)
    qr.add_symbol()
    #print(qr.get_tui_QR())
    #print(qr.QR_list)