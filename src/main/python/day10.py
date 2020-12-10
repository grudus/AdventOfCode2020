def first_star(adapters):
    built_in_adapter = max(adapters) + 3
    adapters = sorted(adapters) + [built_in_adapter]
    used_offsets = {1: 0, 2: 0, 3: 0}
    curr_voltage = 0

    for adapter in adapters:
        diff = adapter - curr_voltage
        used_offsets[diff] += 1
        curr_voltage += diff
    
    return used_offsets[1] * used_offsets[3]


def second_star(adapters):
    built_in_adapter = max(adapters) + 3
    adapters = [0] + sorted(adapters) + [built_in_adapter]
    possibilities_map = find_possibilities(adapters)
    adapter_to_num_of_paths = {built_in_adapter: 1}
    
    for adapter in reversed(sorted(possibilities_map.keys())):
        if adapter == built_in_adapter:
            continue

        possibilities = possibilities_map[adapter]
        adapter_to_num_of_paths[adapter] = sum([adapter_to_num_of_paths[x] for x in possibilities])

    return adapter_to_num_of_paths[0]


def find_possibilities(adapters):
    possibilities_map = {}
    for i, curr_adapter in enumerate(adapters):
        possibilities = [ad for ad in adapters[i+1:i+4] if ad - curr_adapter <= 3]
        possibilities_map[curr_adapter] = possibilities
    
    return possibilities_map
        

if __name__ == "__main__":
    adapters = open('src/main/resources/day10/input.txt', 'r').read().split("\n")
    adapters = list(map(int, adapters))
    print(first_star(adapters))
    print(second_star(adapters))