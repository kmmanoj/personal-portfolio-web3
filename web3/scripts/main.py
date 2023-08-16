from brownie import network, accounts

account = None

def use_sepolia_net():
    if network.show_active() != 'sepolia':
        print('Connecting to sepolia network')
        network.disconnect()
        network.connect('sepolia')
        print('Connected to', network.show_active(), 'network')
    else:
        print('Already connected to Sepolia network')

def load_accounts():
    global account
    if len(accounts) == 0:
        print('No account found. Load account ...')
        accounts.load('kmmanoj-brownie')
    account = accounts[0]

def main():
    use_sepolia_net()
    load_accounts()
