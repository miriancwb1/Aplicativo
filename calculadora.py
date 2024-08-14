class calculadora:
    def soma (self,a,b):
        return a + b 
    
    def subtracao (self,a,b): 
        return a - b 
    

    def multiplicacao(self,a,b):
        return a * b 
    
    def divisao (self, a,b):
        if b == 0: 
            return "Erro: divisao por zero"
        
        return a/b
    


##exemplo de uso das clases 
    
calc_basica = calculadora() 
print ("soma:", calc_basica.soma(10,5))

print ("subtracao.",calc_basica.subtracao(5,2))

print ("multiplicacao:", calc_basica.multiplicacao(10,5))

print ("divisao:",calc_basica.divisao (10,5))

#calc_avancada = calculadora()
#print ("Resto da divisão:", calc_avancada.resto_divisão(10,3))

