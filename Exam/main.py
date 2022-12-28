class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close

    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        return self.targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        pass

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        pass

    def __str__(self):
        # текстовое представление сделки
        pass


def read_data(file_name):
    with open(file_name, 'r') as f:
        content = f.read().splitlines()
    return content


def parse_data(content):
    print(content)
    bank = list()
    entry = list()
    targets = list()
    close = list()

    s_bank = 'Bank: '
    s_entry = 'Entry: '
    s_targets = 'Target: '
    s_close = 'Close: '
    s_usd = 'USD'

    for line in content:
        if line.startswith(s_bank):
            start_index, end_index = line.find(s_bank), line.find(s_usd)
            bank.append(float(line[start_index + len(s_bank):end_index]))
        if line.startswith(s_entry):
            start_index, end_index = line.find(s_entry), line.find(s_usd)
            entry.append(float(line[start_index + len(s_entry):end_index]))
        if line.startswith(s_targets):
            targets.extend([float(x[:-(len(s_usd) + 1)]) for x in line.split()[1:]])
        if line.startswith(s_close):
            start_index, end_index = line.find(s_close), line.find(s_usd)
            close.append(float(line[start_index + len(s_close):end_index]))
    return (bank, targets, entry, close)


def write_data(file_name, data):
    pass


def main():
    content = read_data('deals.txt')
    result = parse_data(content)
    strategy_deal = StrategyDeal(*result)
    # print(strategy_deal.bank)
    # print(strategy_deal.entry)
    # print(strategy_deal.targets)
    # print(strategy_deal.close)
    # write_data('out.txt', result)


if __name__ == '__main__':
    main()

# INPUT FILE deal.txt:
