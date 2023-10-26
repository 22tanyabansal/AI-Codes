def calculate_confidence(itemset_A, itemset_B, transactions):
    support_A = sum(1 for transaction in transactions if itemset_A.issubset(transaction))
    support_union = sum(1 for transaction in transactions if itemset_A.union(itemset_B).issubset(transaction))
    return support_union / support_A if support_A > 0 else 0

def load_data():
    # Sample transaction data (list of sets)
    return [
        {'bread', 'milk', 'eggs'},
        {'eggs', 'sugar', 'coffee'},
        {'bread', 'sugar', 'milk', 'coffee'},
        {'bread', 'milk', 'sugar', 'eggs'},
        {'coffee', 'sugar', 'eggs'}
    ]

def find_frequent_itemsets(transactions, min_support):
    itemsets = [{item} for transaction in transactions for item in transaction]
    frequent_itemsets = []
    while itemsets:
        item_counts = {tuple(itemset): sum(1 for transaction in transactions if set(itemset).issubset(transaction)) for itemset in itemsets}
        frequent_itemsets.extend([set(itemset) for itemset, count in item_counts.items() if count >= min_support])
        itemsets = [set(itemset1.union(itemset2)) for idx, itemset1 in enumerate(frequent_itemsets) for itemset2 in frequent_itemsets[idx + 1:] if len(itemset1.union(itemset2)) == len(itemset1) + 1]
    return frequent_itemsets


def generate_association_rules(frequent_itemsets, transactions, min_support, min_confidence):
    return [(item_A, itemset - item_A, sum(1 for transaction in transactions if itemset.issubset(transaction)), calculate_confidence(item_A, itemset - item_A, transactions))
            for itemset in frequent_itemsets if len(itemset) > 1
            for item_A in itemset if calculate_confidence({item_A}, itemset - {item_A}, transactions) >= min_confidence and sum(1 for transaction in transactions if itemset.issubset(transaction)) >= min_support]

# Example usage
if __name__ == "__main__":
    transactions = load_data()
    min_support = 2  # Minimum support count
    min_confidence = 0.1  # Minimum confidence threshold
    
    frequent_itemsets = find_frequent_itemsets(transactions, min_support)
    
    # Generate and print association rules based on confidence threshold and support count
    association_rules = generate_association_rules(frequent_itemsets, transactions, min_support, min_confidence)
    
    for item_A, item_B, support, confidence in association_rules:
        print(f"Rule: {item_A} -> {item_B}")
        print(f"Support: {support}, Confidence: {confidence:.2f}")
        print("-----------")

