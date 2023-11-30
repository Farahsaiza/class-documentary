class documentaire ():
    #class attribut
    _count=0
    #constructor
    def __init__(self, title, date):
       
        self._title = title
        self._date  = date
        documentaire._count= documentaire._count+1
        
    
    # getters
    def getcode(self):
        return self._code
    
    def gettitle(self):
        return self._title

    def getdate(self):
        return self._date
    
    #class methode
    def getcount(self):
        return documentaire._count
    
    #setters
    def setcode(self,code):
        self._code= code

    def settitle(self,title):
        self._title= title

    def setdate(self,date):
        self._date = date


    def ToString(self):
        print(" le titre est:{}, la date du sortie est:{}".format( self.gettitle(), self.getdate()))

    def count(self):
        print("votre code est{}".format(self.getcount()))

class exemplaire(documentaire):
    def __init__(self,title,date, num, date_achat):
        super().__init__(title,date)
        self.__num = num
        self.__date_achat = date_achat
    
    #getters
    def getnum(self):
        return self.__num
    
    def getachat(self):
        return self.__date_achat
    
    #setters
    def setnum(self,num):
        self.__num= num
    
    def setachat(self, date_achat):
        self.__date_achat=date_achat

    def ToString(self):
        print(" le titre est:{}, la date du sortie est:{},le numeroest{}, etla date d'achat est{}".format( self.gettitle(), self.getdate(), self.getnum(),self.getachat()))

    def Equals(self,exempl1):
        if self.getnum()==exempl1.getnum():
            return True
        else:
            return False


d1=exemplaire( "farah" ,"31.01.2002", 3456,"54.98.456")


d1.ToString()
d1.count()

d2=exemplaire("wissal", "25.09.2004",234,"567.890.4")



d2.ToString()
print(d2.Equals(d1))
d2.count()


