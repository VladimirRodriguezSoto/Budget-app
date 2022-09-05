class Category:
  
    def __init__(self,descripcion):
        self.descripcion = descripcion
        self.ledger=[]
        self.balance=0.0
      
    def __repr__(self):
        ledger=''
        titulo=self.descripcion.center(30, "*")+"\n"
        for item in self.ledger:
            linea_descripcion="{:<23}".format(item["description"])
            linea_cantidad="{:>7.2f}".format(item["amount"])
            ledger+="{}{}\n".format(linea_descripcion[:23],linea_cantidad[:7])
        Total="Total: {:.2f}".format(self.balance)
        return titulo+ledger+Total
  
    def deposit(self,amount, descripcion=""):
        self.ledger.append({"amount":amount,"description":descripcion})
        self.balance+=amount
    
    def withdraw(self,amount,descripcion=""):
        if self.balance-amount>=0:
          self.ledger.append({"amount": -1* amount,"description":descripcion})
          self.balance-=amount
          return True
        else:
          return False
    
    def get_balance(self):
        return self.balance

    def transfer(self,amount,categoria):
        if self.withdraw(amount, "Transfer to {}".format(categoria.descripcion)):
          categoria.deposit(amount, "Transfer from {}".format(self.descripcion))
          return True
        else:
          return False
          
    def check_funds(self,amount):
        if self.balance>=amount:
          return True
        else:
          return False



def create_spend_chart(categorias):
    gasto=[]
#-------Se recorren las categorias 
    for categoria in categorias:
        gasto_categoria=0
#--------Se recorren los objetos de las categorias
        for item in categoria.ledger:
            if item["amount"]<0:
              gasto_categoria+=abs(item["amount"])
        gasto.append(round(gasto_categoria,2))
#--------Se calculan los porcentajes por categoria
    gasto_total=round(sum(gasto),2)
    gasto_porcentaje=list(map(lambda amount:int((((amount/gasto_total)*10)//1)*10),gasto))
#-------- Se crea la tabla
    titulo="Percentage spent by category\n"
    chart=""
    for x in reversed(range(0,101,10)):
        chart+=str(x).rjust(3) + '|'
        for porcentaje in gasto_porcentaje:
            if porcentaje>=x:
                chart+=" o "
            else:
                chart += "   "
        chart+=" \n"
    pie_grafica = "    " + "-" * ((3 * len(categorias)) + 1) + "\n"
    descripciones=list(map(lambda categoria:categoria.descripcion,categorias))
    max_length = max(map(lambda descripcion: len(descripcion), descripciones))
    descripciones = list(map(lambda descripcion: descripcion.ljust(max_length), descripciones))
    for n in zip(*descripciones):
        pie_grafica += "    " + "".join(map(lambda s: s.center(3), n)) + " \n"

    return (titulo + chart + pie_grafica).rstrip("\n")