class Author:
    all = []
    def __init__(self,name):
        if isinstance(name,str):
           self.name = name
        Author.all.append(self)
    def contracts(self):
        all_contracts = Contract.all
        contracts = []
        for contract in all_contracts:
            if contract.author == self:
                 contracts.append(contract)
        return contracts
    def books(self):
        all_contracts = Contract.all
        books = []
        for contract in all_contracts:
            if contract.author == self:
                books.append(contract.book)
        return books
    def sign_contract(self,book,date,royalties):
        return Contract(self,book,date,royalties)
    
    def total_royalties(self):
        all_contracts = Contract.all
        rayalties_for_author = []
        for contract in all_contracts:
            if contract.author == self:
                rayalties_for_author.append(contract.royalties)
        return sum(rayalties_for_author)
             
       
             
   
        


class Book:
    all = []
    def __init__(self,title):
        if isinstance(title,str):
            self.title = title
        Book.all.append(self)
    def contracts(self):
       all_contracts = Contract.all
       contracts_for_book = []
       for contract in all_contracts:
          if contract.book == self:
             contracts_for_book.append(contract)
       return contracts_for_book
    def authors(self):
       all_contracts = Contract.all
       authors_for_book = []
       for contract in all_contracts:
          if contract.book == self:
             authors_for_book.append(contract.author)
       return authors_for_book

             


class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        self.book = book
        self.author = author
        self.royalties = royalties
        self.date = date
        Contract.all.append(self)
    @property
    def author(self):
      return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
          self._author = author
        else:
          raise Exception('The author must be an instance of the Author Class')
   
    @property
    def book(self):
      return self._book
    
    @book.setter
    def book(self,book):
        if isinstance(book,Book):
          self._book = book
        else:
           raise Exception('The book must be an instance of the Book class ')
   
    @property
    def date(self):
      return self._date
    @date.setter
    def date(self,date):
        if isinstance(date,str):
          self._date = date
        else:
           raise Exception('The date must be string')
   
       
     
    @property
    def royalties(self):
      return self._royalties
    
    @royalties.setter
    def royalties(self,royalties):
        if isinstance(royalties,int):
          self._royalties = royalties
        else:
           raise Exception('The royalties must be an integer')
        
    @classmethod
    def contracts_by_date(self,date):
        all_contarcts= Contract.all
        contracts_to_return = []
        for contract in all_contarcts:
            if contract.date == date:
                contracts_to_return.append(contract)
        return contracts_to_return
               
          
   