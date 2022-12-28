class StrategyDeal:
    def __init__(self, *, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close


class StrategyDeals:
    def __init__(self):
        self.deals = list()

    def add_deal(self, deal):
        self.deals.append(deal)

    # handlers
    def get_closes(self):
        all_closes = [getattr(self.deals[x], 'close') for x in range(len(self.deals))]
        return all_closes

    def get_banks(self):
        all_banks = [getattr(self.deals[x], 'bank') for x in range(len(self.deals))]
        return all_banks

    def get_entries(self):
        all_entries = [getattr(self.deals[x], 'entry') for x in range(len(self.deals))]
        return all_entries

    # add attributes
    deals = None
    targets = None
    percents = None
    banks = None
    entries = None
    closes = None
    target_banks = None
    content = None

    # main task
    def get_targets(self):
        # вернуть список таргетов в виде числовых значений float [21.5, 22.8, 23.5]
        all_targets = [getattr(self.deals[x], 'targets') for x in range(len(self.deals))]
        return all_targets

    def get_target_percents(self):
        # вернуть список процентов, как в примере, округленные до 3 знака [6.912, 13.376, 16.857]
        # target to entry and return tuples
        result = list()

        for i in range(len(self.entries)):
            inter_result = list()
            for j in range(len(self.targets[i])):
                inter_result.append(round((self.targets[i][j] / self.entries[i] - 1) * 100, 3))
            result.append(inter_result)

        return result

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        result = list()
        for i in range(len(self.banks)):
            inter_result = list()
            for j in range(len(self.percents[i])):
                inter_result.append(round(self.banks[i] * (100 + self.percents[i][j]) / 100, 3))
            result.append(inter_result)

        return result

    def prepare_string(self):
        # текстовое представление сделки

        results = list()  # list with all deals

        # looping through first
        for i in range(len(self.banks)):
            result_template_target = list()
            inter_result = list()
            inter_result.extend([self.banks[i], self.entries[i], self.closes[i], self.targets[i], self.percents[i],
                                 self.target_banks[i]])
            template = """\
BANK: {}
START_PRICE: {}
STOP_PRICE: {}\
""".format(inter_result[0], inter_result[1], inter_result[2])

            # looping through second
            for j in range(len(inter_result[3])):
                template_target = """
{} target: {}
Percent: {}%
Bank: {}
""".format(j + 1, inter_result[3][j], inter_result[4][j], inter_result[5][j])
                # 2nd loop
                result_template_target.append(template_target)
            # 1st loop
            results.append('\n'.join([template, ''.join(result_template_target)]))
        # out of loops
        content = '\n-----\n\n'.join(results)

        return content

    def __str__(self):
        # текстовое представление сделки
        return self.content


def parse_data(content):
    s_bank = 'Bank: '
    s_entry = 'Entry: '
    s_targets = 'Target: '
    s_close = 'Close: '
    s_usd = 'USD'

    strategy_deals = StrategyDeals()

    if len(content) != 0:
        content.append('-----')

    # read data
    for line in content:
        if line.startswith(s_bank):
            start_index, end_index = line.find(s_bank), line.find(s_usd)
            bank = float(line[start_index + len(s_bank):end_index])
        elif line.startswith(s_entry):
            start_index, end_index = line.find(s_entry), line.find(s_usd)
            entry = float(line[start_index + len(s_entry):end_index])
        elif line.startswith(s_targets):
            targets = []
            for n in [x[:-(len(s_usd) + 1)] for x in line.split()[1:]]:
                if n.endswith(';'):
                    targets.append(float(n[:-1]))
                else:
                    targets.append(float(n))
        elif line.startswith(s_close):
            start_index, end_index = line.find(s_close), line.find(s_usd)
            close = float(line[start_index + len(s_close):end_index])
        elif line.startswith('-----'):
            deal = StrategyDeal(bank=bank, entry=entry, targets=targets, close=close)
            strategy_deals.add_deal(deal)

    return strategy_deals


def read_data(file_name):
    with open(file_name, 'r') as f:
        content = f.read().splitlines()
    return content


def write_data(file_name, data):
    with open(file_name, 'w') as f:
        f.write(data)


def main():
    # load and parse the data
    content = read_data('deals.txt')
    strategy_deals = parse_data(content)

    # add attributes
    StrategyDeals.targets = strategy_deals.get_targets()
    StrategyDeals.banks = strategy_deals.get_banks()
    StrategyDeals.closes = strategy_deals.get_closes()
    StrategyDeals.entries = strategy_deals.get_entries()

    StrategyDeals.percents = strategy_deals.get_target_percents()
    StrategyDeals.target_banks = strategy_deals.get_target_banks()

    # add content as attribute
    content = strategy_deals.prepare_string()
    StrategyDeals.content = content

    # usage
    write_data('out.txt', content)
    print(strategy_deals)

    # tests
    # print(StrategyDeals.targets)
    # print(StrategyDeals.percents)
    # print(StrategyDeals.target_banks)

    # flattened
    from itertools import chain
    # print(list(chain(*StrategyDeals.targets)))
    # print(list(chain(*StrategyDeals.percents)))
    # print(list(chain(*StrategyDeals.target_banks)))


if __name__ == '__main__':
    main()
