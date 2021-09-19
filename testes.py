'''
class DosagemMath():
    def __init__(self,alfa=0.35,alfa_novo=0,m=5,massa_pedra=30,ac=0.6):
        self.alfa=alfa
        self.alfa_novo=alfa_novo
        self.m=m
        self.massa_pedra=massa_pedra
        self.ac=ac
   
    def traco_dosagem_a(self):
        a=self.alfa*(1+self.m)-1
        return round(a,2)
   
    def traco_dosagem_p(self):
        a=(self.alfa*self.m)+(self.alfa*1)-1
        p=a-self.m
        return abs(round(p,2))
   
    def massa_cimento(self):
        a=self.alfa*(1+self.m)-1
        p=self.m-a
        massa_areia=(self.massa_pedra*a)/p
        massa_cimento=(self.massa_pedra)/p
        massa_agua=self.ac*massa_cimento
        return round(massa_cimento,2)
   
   
    def massa_areia(self):
        a=self.alfa*(1+self.m)-1
        p=self.m-a
        massa_areia=(self.massa_pedra*a)/p
        massa_cimento=(self.massa_pedra)/p
        massa_agua=self.ac*massa_cimento
        return round(massa_areia,2)
   
    def massa_agua(self):
        a=self.alfa*(1+self.m)-1
        p=self.m-a
        massa_areia=(self.massa_pedra*a)/p
        massa_cimento=(self.massa_pedra)/p
        massa_agua=self.ac*massa_cimento
        return round(massa_agua,2)
   
    def massa_acres_agua(self):
        a=self.alfa*(1+self.m)-1
        p=self.m-a
        massa_areia=(self.massa_pedra*a)/p
        massa_cimento=(self.massa_pedra)/p
        massa_agua=self.ac*massa_cimento
       
        a_novo=self.alfa_novo*(1+self.m)-1
        p_novo=self.m-a_novo
        massa_areia_novo=(self.massa_pedra*a_novo)/p_novo
        massa_cimento_novo=(self.massa_pedra)/p_novo
        massa_agua_novo=self.ac*massa_cimento_novo
        massa_acres_agua=(massa_agua_novo-massa_agua)
        return round(massa_acres_agua,2)
   
    def massa_acres_cimento(self):
        a=self.alfa*(1+self.m)-1
        p=self.m-a
        massa_areia=(self.massa_pedra*a)/p
        massa_cimento=(self.massa_pedra)/p
        massa_agua=self.ac*massa_cimento
       
        a_novo=self.alfa_novo*(1+self.m)-1
        p_novo=self.m-a_novo
        massa_areia_novo=(self.massa_pedra*a_novo)/p_novo
        massa_cimento_novo=(self.massa_pedra)/p_novo
        massa_agua_novo=self.ac*massa_cimento_novo
        massa_acres_cimento=(massa_cimento_novo-massa_cimento)
        return round(massa_acres_cimento,2)
   
    def massa_acres_areia(self):
        a=self.alfa*(1+self.m)-1
        p=self.m-a
        massa_areia=(self.massa_pedra*a)/p
        massa_cimento=(self.massa_pedra)/p
        massa_agua=self.ac*massa_cimento
       
        a_novo=self.alfa_novo*(1+self.m)-1
        p_novo=self.m-a_novo
        massa_areia_novo=(self.massa_pedra*a_novo)/p_novo
        massa_cimento_novo=(self.massa_pedra)/p_novo
        massa_agua_novo=self.ac*massa_cimento_novo
        massa_acres_areia=(massa_areia_novo-massa_areia)
        return round(massa_acres_areia,2)
   
   
    

a = DosagemMath(alfa_novo=0.37)

print(a.massa_areia())
print(a.massa_acres_areia())

'''


'''
linhas = [11,22,33]
a = [10,20,30,40]
b = [100,200,300,400]
c = [101,202,303,404]


for i in range(len(linhas)):
    print(i+1, a[i], b[i], c[i])

'''


'''
def colunas_db(linhas):
    contador = 0
    indice = []
    a = []
    b = []
    c = []
    for i in linhas:

        a.append(i[1])
        b.append(i[2])
        c.append(i[3])
        indice.append(contador+1)
        contador = contador+1
    return[indice,a,b,c]
a = [(7,10,100,1000),(8,20,200,2000),(9,30,300,3000)]

resultado = colunas_db(a)
print(resultado)
print("\n ja rodou")

'''
            




