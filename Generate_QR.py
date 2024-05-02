from pprint import pprint
import re
import numpy as np
from QR_parameter import Generate_parameter,QR_parameter
import pandas as pd
import os
class QR():
    def __init__(self,QR_parm:Generate_parameter):
        self.matrix=QR_parm.matrix
        self.QR_list=np.zeros((self.matrix,self.matrix))
        self.pram=QR_parm
        self.QR_pram=QR_parameter()
    def generate_QR(self):
        #モード設定
        self.__set_mode()
        #入力文字数がオーバーしてないかチェック
        self.validate_inp()
        self.__set_char_counter()
        return
    def __check_capacity(self):
        mode=self.QR_pram.mode
        v_table=pd.read_csv('version_table.csv')
        v1=v_table[v_table['version']==self.pram.versinon]
        v1=v1[v1["ECL"]==self.pram.error_level]
        if mode==0b0001:
            v1=v1['NM']
        elif mode==0b0010:
            v1=v1['AL']
        else:
            v1=v1['8B']
        return v1.values
    def validate_inp(self):
        self.__set_mode()
        capa=self.__check_capacity()[0]
        if len(self.pram.input)>capa:
            print("Capacity over!!!")
            return
        else:
            print("mode:"+str(self.QR_pram.mode))
            print(str(len(self.pram.input))+'/'+str(capa))
    def __set_mode(self):
        inp=self.pram.input
        am = re.compile('[a-zA-Z0-9]+')
        nm = re.compile('[0-9]+')
        mode:int=0b0001
        if nm.fullmatch(inp):
            mode=0b0001
        elif am.fullmatch(inp):
            mode=0b0010
        else:
            mode=0b0100
        self.QR_pram.mode=mode
    def __set_char_counter(self):
        mode=self.QR_pram.mode
        counter=len(self.pram.input)
        if mode==0b0001:
            counter=format(counter,'010b')

        elif mode==0b0010:
            counter=format(counter,'09b')
        else:
            counter=format(counter,'08b')
        print(counter)
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

    print()
    Qp=Generate_parameter("ああああ")
    Qp.versinon=1
    qr=QR(Qp)
    qr.generate_QR()
    #qr.validate_inp()
    #qr.add_symbol()
    #print(qr.get_tui_QR())
    #print(qr.QR_list)