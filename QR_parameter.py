class Generate_parameter():
    def __init__(self,inp,version:int=1,error_level:str="H") -> None:
        self.versinon:int=version
        self.matrix:int=(self.versinon-1)*4+21
        self.error_level:str=error_level
        self.input=inp
class QR_parameter():
    def __init__(self) -> None:
        self.mode:int=0b0001
        self.char_counter:int=0b0