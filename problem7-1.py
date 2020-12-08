def parse_rule(rule):
  key, value = rule.split("contain")
  key = key.strip().replace(" bags", "").replace(" bag", "")
  value = [' '.join(v.split(" ")[2:]).replace(".", "").replace(" bags", "").replace(" bag", "").strip() for v in value.split(",") if len(v) > 0]
  return key, value

def check_rule(rules, string, complete=[]):
    new = [key for key,value in rules.items() if any([string in v for v in value])]
    print("%s bag: \n|-%s" % (string, ("\n|-".join(new) if len(new) > 0 else 'END_OF_BAGS')))
    for bag in new:
        complete.extend(check_rule(rules, bag, complete))
    complete.extend(new)
    return set(complete)

def main():
    rules = {k:v for (k,v) in [parse_rule(rule) for rule in open('input7.txt', 'r').readlines() if len(rule.split("contain")) > 1]}
    complete = check_rule(rules, "shiny gold")
    print(len(complete))

if __name__ == '__main__':
    main()
