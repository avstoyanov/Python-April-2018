class Bank_Account:
    def __init__(self, name, balance, bank):
        self.name = name
        self.balance = balance
        self.bank = bank

r_inp = input()
i_list = []
i = 0
while r_inp != "end":
    n_bank, p_name, a_bal = r_inp.split(" | ")
    account = Bank_Account(p_name, a_bal, n_bank)
    i_list[i] = account