import operator
possible_sums = {}

with open("right-triangles.txt") as f:
    right_triangle_ratios = f.readlines()
right_triangle_ratios = [x.strip().replace("\t", "").replace(" ", "") for x in right_triangle_ratios] 

for ratio in right_triangle_ratios:
	p = sum(list(map(int, ratio.split(":"))))
	p_multiple = p
	while (p_multiple <= 1000):
		if not p_multiple in possible_sums:
			possible_sums[p_multiple] = 1
		else:
			possible_sums[p_multiple] += 1
		p_multiple += p

sorted_sums = sorted(possible_sums.items(), key=operator.itemgetter(1))
print(sorted_sums)