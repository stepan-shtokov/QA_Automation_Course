def remove_duplicates(tickets):
    for key in tickets:
        tickets[key] = list(set(tickets[key]))
    return tickets

def map_tickets_by_type(types, tickets):

    tickets = remove_duplicates(tickets)
    tickets_by_type = {}

    for key, value in tickets.items():
        ticket_type = types[key]
        if ticket_type not in tickets_by_type:
            tickets_by_type[ticket_type] = value
        else:
            tickets_by_type[ticket_type] += [x for x in value if x not in tickets_by_type[ticket_type]]

    return tickets_by_type

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = map_tickets_by_type(types, tickets)

for key, value in tickets_by_type.items():
    print(f'{key}: {value}')