from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self,name=None,age=None):
        self._name = name
        self._age = age

    @property
    @abstractmethod
    def name(self): ...

    @property
    @abstractmethod
    def age(self): ...

    def __repr__(self):
        return f'{ self.__class__.__name__} ({self._name},{self._age})'
#Pessoa (Vilner César, 21)

class Conta(ABC):
    def __init__(self,agency=None,number_account = None):
        self.agency = agency
        self.number_account = number_account
        self._bank_balance = 0

    @property
    def bank_balance(self):
        return self._bank_balance

    def deposit(self,bank_balance):
        self._bank_balance = bank_balance
   
    def account_add(self,agency,number_account): ...

    @abstractmethod
    def withdraw_money(self,valor): ...

    def __repr__(self):
        return f'{ self.__class__.__name__} (Agência = {self.agency} ,Número da Conta = {self.number_account}, Saldo = {self._bank_balance})'

class Cliente(Pessoa):
    
    def __init__(self, name=None, age=None):
        super().__init__(name, age)
        self.bank_accountPupanca = None
        self.bank_accountCorrente = None

    
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age

    
    

class ContaCorrente(Conta):
    def __init__(self, agency=None, number_account=None):
        super().__init__(agency, number_account)
        self._limit = 200
        


    @property
    def limit(self):
        return self._limit
    
    @limit.setter
    def limit(self,valor):
        self._limit = valor



    def check_withdraw(self,valor):

        if valor <= 0 or valor > self.limit:
            return False
        else:
            return True

    def withdraw_money(self,valor):
    
        if self.check_withdraw(valor):
            self._limit -= valor
            self._bank_balance -= valor
        else:
            print(f'Desculpe, você atingiu seu limite saque. Seu saldo é {self.bank_balance} \n' , f'limite {self._limit}')

    
class ContaPoupanca(Conta):
    def __init__(self, agency, number_account):
        super().__init__(agency, number_account)

    def check_withdraw(self,valor):
        if valor <= 0 or valor > self.bank_balance:
            return False
        else:
            return True

    def withdraw_money(self,valor):
        if self.check_withdraw(valor):
            self._bank_balance -= valor 

class Banco:
    def __init__(self):
        self.name = 'Banco Do Vilneco'
        self.bank_angency = '1668-3'
        self.bank_accounts = []
        self.clients = []

    def create_ContaPoupanca(self,obj_client,number_account):
        agency = self.bank_angency
        conta = ContaPoupanca(agency,number_account)
        self.clients.append(obj_client)
        obj_client.bank_accountPupanca = conta
        
    
    def create_ContaCorrente(self,obj_client,number_account):
        agency = self.bank_angency
        conta = ContaCorrente(agency,number_account)
        self.clients.append(obj_client)
        self.bank_accounts.append(conta)
        obj_client.bank_accountCorrente = conta

    

    def __repr__(self):
        return f'Banco: {self.name} \n Agência: {self.bank_angency} \n Clientes que possuem conta nesse banco: {self.clients}'
        

cliente = Cliente('Vilner César', 21)


banco = Banco()
banco.create_ContaCorrente(cliente, '58784-X')
'''cliente.bank_accountCorrente.withdraw_money(200)
print(cliente.bank_accountCorrente.limit)'''