class Conversor:
    
    @classmethod
    def celsiusParaFahreheit(self,temp):
        return temp*9.0/5 + 32
    
    @classmethod
    def fahrenheitParaCelsius(self,temp):
        return (temp - 32.0)*5.0/9.0
