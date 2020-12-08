def parse_rule(rule):
    key, value = rule.split("contain")
    key = key.strip().replace(" bags", "").replace(" bag", "")
    value = [' '.join(v.split(" ")).replace(".", "").replace(" bags", "").replace(" bag", "").strip() for v in value.split(",") if len(v) > 0]
    return key, value

def check_bag(rules, bag_name):
    new = [value for key,value in rules.items() if bag_name == key][0]
    if 'no other' in new:
        return 1
    else:
        bags = {' '.join(i.split(" ")[1:]):int(i.split(" ")[0]) for i in new}
        inner_bags = []
        for bag, count in bags.items():
            new_val = check_bag(rules, bag)
            inner_bags.append(count * new_val + count if new_val != 1 else count * new_val)
        return sum([bag for bag in inner_bags])

def main():
    rules = {k:v for (k,v) in [parse_rule(rule) for rule in open('input7.txt', 'r').readlines() if len(rule.split("contain")) > 1]}
    cumulative_bags = check_bag(rules, "shiny gold")
    print(cumulative_bags)

if __name__ == '__main__':
    main()
