from abc import ABC, abstractmethod


class Pessoa():
    def __init__(self,name=None,age=None):
        self._name = name
        self._age = age

    @property
    def name(self): ...

    @property
    def age(self): ...

    def __repr__(self):
        return f'{ self.__class__.__name__} ({self._name!r},{self._age!r})'
#Pessoa (Vilner César, 21)

class Conta(ABC):
    def __init__(self,agency=None,number_account = None):
        self.agency = agency
        self.number_account = number_account
        self._bank_balance = 0

    @property
    def bank_balance(self):
        return self._bank_balance

    @abstractmethod
    def withdraw_money(self,valor): ...
    
    def deposit(self,value):
        self._bank_balance += value
   
    def account_add(self,agency,number_account): ...



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
            return True
        else:
            print(f'Desculpe, você não pode sacar esse valor. Seu saldo é {self.bank_balance} \n' , f'limite: {self._limit}')
            return False

    
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
            return True
        else:
            print(f'Desculpe, você não pode sacar esse valor. Seu saldo é: {self.bank_balance}')
            return False 

class Banco:
    def __init__(self):
        self.name = 'Banco Do Vilneco'
        self.bank_angency = 16683
        self.bank_accounts = []
        self.clients = []

    def create_ContaPoupanca(self,obj_client,number_account):
        agency = self.bank_angency
        conta = ContaPoupanca(agency,number_account)
        self.clients.append(obj_client)
        self.bank_accounts.append(conta)
        obj_client.bank_accountPupanca = conta
        
    
    def create_ContaCorrente(self,obj_client,number_account):
        agency = self.bank_angency
        conta = ContaCorrente(agency,number_account)
        self.clients.append(obj_client)
        self.bank_accounts.append(conta)
        obj_client.bank_accountCorrente = conta

    def check_client_MyBank(self,client: Cliente):

        for client_myBank in self.clients:
            if  client_myBank.name == client.name:
                return True
   
    def check_accountMyBankCorrente(self,obj_client):
        for account in self.bank_accounts:
            if obj_client.bank_accountCorrente.number_account == account.number_account:
                return False

    def check_accountMyBankPoupanca(self,obj_client):
        for account in self.bank_accounts:
            if obj_client.bank_accountCorrente.number_account == account.number_account:
                return False
    
    def authenticate(self,obj_client,accoutType):
        if accoutType.upper() != 'CC' and accoutType.upper() != 'CP':
            print(accoutType.upper())
            return False

        if accoutType.upper() == 'CC':
            if obj_client.bank_accountCorrente == None:
                return False
  
            if not self.check_client_MyBank(obj_client):
                return False
            
            if obj_client.bank_accountCorrente.agency != self.bank_angency:
                return False
        
        if accoutType.upper() == 'CP':
            if obj_client.bank_accountPupanca == None:
                return False
  
            if not self.check_client_MyBank(obj_client):
                return False
            
            if obj_client.bank_accountPupanca.agency != self.bank_angency:
                return False
       
        return True    
            

    def deposit_bank(self,obj_client,accountType,valor):
        
        if accountType.upper() == 'CC':

            if self.authenticate(obj_client,accountType):
                obj_client.bank_accountCorrente.deposit(valor)
                print(f'Parabéns, você acabou de despositar {valor}. Seu saldo é: {obj_client.bank_accountCorrente.bank_balance} ')
            
            else:
                print('Não foi possível realizar o deposito. Usuário não atenticado, tente novamente mais tarde.')
        
        if accountType.upper() == 'CP':

            if self.authenticate(obj_client,accountType):
                obj_client.bank_accountPupanca.deposit(valor)
                print(f'Parabéns, você acabou de despositar {valor}R$. Seu saldo é: {obj_client.bank_accountPupanca.bank_balance}R$')
            
            else:
                print('Não foi possível realizar o deposito. Usuário não atenticado, tente novamente mais tarde.')
        
                    
           

    def withdraw_moneyBank(self,obj_client ,accoutType,value):
        
        if accoutType.upper() == 'CC':
            
            if self.authenticate(obj_client,accoutType):   
                obj_client.bank_accountCorrente.withdraw_money(value)
                print(f'Saque liberado, você sacou {value}R$')
            else:
                print(f'Você não realizar um saque nesse banco. Usuário não autenticado')
        
        if accoutType.upper() == 'CP':
            if self.authenticate(obj_client,accoutType):   
                if obj_client.bank_accountPupanca.withdraw_money(value):
                    print(f'Saque liberado, você sacou {value}R$')
                else: 
                    print(f'Saque não realizado')
            else:
                print(f'Você não realizar um saque nesse banco. Usuário não autenticado')

        

    def __repr__(self):
        return f'Banco: {self.name} \n Agência: {self.bank_angency} \n Clientes que possuem conta nesse banco: {self.clients}'
        

cliente = Cliente('Vilner César', 21)
cliente2 = Cliente('seu João', 45)

banco = Banco()
banco.create_ContaPoupanca(cliente, 527840)

banco.deposit_bank(cliente,'CP',100)
banco.withdraw_moneyBank(cliente,'CP',100)
banco.withdraw_moneyBank(cliente,'CP',0.5)
print(cliente)
