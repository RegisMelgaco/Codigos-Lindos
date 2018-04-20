def multi_karatsuba(n1, n2, chamada=1):
	#print("-----",  chamada,"-----")
	l1 = len(str(n1))
	l2 = len(str(n2))

	#print("l1:", l1)
	#print("l2:", l2)

	if l1 == 1 or l2 == 1:
		return n1 * n2
	else:
		if l1 < l2:
			mid = l1 // 2
		else:
			mid = l2 // 2

	mid = 10**mid

	#print("mid:", mid)

	a = n1 // mid
	b = n1 - a * mid
	c = n2 // mid
	d = n2 - c * mid

	#print("a:", a, "b:", b, "c:", c, "d:", d)

	z0 = multi_karatsuba(a, c, chamada+1)
	z2 = multi_karatsuba(b, d, chamada+1)
	z1 = multi_karatsuba(a+b, c+d, chamada+1) - z0 - z2

	#print("z0:", z0, "z1:", z1, "z2", z2)

	return (z0*(mid**2)) + (z1*mid) + z2


n1 = int(input("Dê entrada do primeiro numero da multiplicação: "))
n2 = int(input("Dê entrada do segundo numero da multiplicação: "))

print(multi_karatsuba(n1, n2))