import sys
from collections import defaultdict


def bank_account(operations):
    result = []
    clients = defaultdict(int)
    for operation in operations:
        operation_name = operation[0]
        if operation_name == 'INCOME':
            percent = int(operation[1])
            for client_name in clients:
                balance = clients[client_name]
                if balance > 0:
                    clients[client_name] += balance * percent // 100
        else:
            client = operation[1]
            if operation_name == 'BALANCE':
                result.append(clients[client] if client in clients else 'ERROR')
            elif operation_name == 'WITHDRAW':
                clients[client] -= int(operation[2])
            elif operation_name == 'DEPOSIT':
                clients[client] += int(operation[2])
            else:
                second_client = operation[2]
                amount = int(operation[3])
                clients[client] -= amount
                clients[second_client] += amount
    return result

operations = [line.split() for line in sys.stdin]

results = bank_account(operations)

for result in results:
    print(result)
