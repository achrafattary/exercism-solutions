from operator import index


def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        count = 0
        for index,char in enumerate(list(strand_a)) :
            if strand_b[index] != char:
                count += 1
        return count

