from models.cliente import Cliente
from models.conta import Conta


rodrigo: Cliente = Cliente('Rodrigo', 'rodrigo@gmail.com', '123.456.789.0', '02/06/1991')

print(rodrigo)

contaf: Conta = Conta(rodrigo)
print(contaf)

