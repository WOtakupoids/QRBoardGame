class QR_parameter():
    def __init__(self,version:int=1) -> None:
        self.versinon:int=version
        self.matrix:int=(self.versinon-1)*4+21