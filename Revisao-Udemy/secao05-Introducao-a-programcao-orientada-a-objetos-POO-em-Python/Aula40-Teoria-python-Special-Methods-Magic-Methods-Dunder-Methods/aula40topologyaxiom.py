from itertools import chain, combinations

def partitions(set_):
    """Yield the list of all partitions of a set."""
    if not set_:
        yield []
        return
    first = next(iter(set_))
    for smaller in partitions(set_ - {first}):
        # Insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [{first} | subset] + smaller[n+1:]
        # Put `first` in its own subset 
        yield [{first}] + smaller

def all_subsets(ss):
    """Return all subsets of a set `ss`."""
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

class Topology:
    def __init__(self, space, subsets):
        self.space = set(space)
        self.subsets = [set(subset) for subset in subsets]
        
        if not self.is_topology():
            raise ValueError("Provided subsets do not form a topology on the given space.")
    
    def is_topology(self):
        # Axiom 1: Check if the space and the empty set are in subsets
        if set() not in self.subsets or self.space not in self.subsets:
            return False
        
        # Axiom 2: Check if the union of any subsets is in subsets
        from itertools import chain, combinations
        all_unions = chain.from_iterable(combinations(self.subsets, r) for r in range(len(self.subsets)+1))
        for union in all_unions:
            union_set = set().union(*union)
            if union_set not in self.subsets:
                return False
        
        # Axiom 3: Check if the intersection of any finite number of subsets is in subsets
        from itertools import combinations
        for r in range(2, len(self.subsets)+1):  # Start from 2 because intersection of one set is the set itself
            for intersection in combinations(self.subsets, r):
                intersection_set = set.intersection(*intersection)
                if intersection_set not in self.subsets:
                    return False
        
        return True

    def __str__(self):
        return f"Topology on {self.space} with subsets {self.subsets}"

# Example usage
set_n = {1, 2, 3}
all_partitions = list(partitions(set_n))
for index, part in enumerate(all_partitions):
    print(f"Partition {index + 1}: {part}")
    for subset in all_subsets(part):
        print(f"  Subset: {subset}")

# for subsets in all_partitions:
#     try:
#         topology = Topology(set_n, subsets)
#         print(topology)
#     except ValueError as e:
#         print(e)

