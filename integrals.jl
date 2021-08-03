e = MathConstants.e

n = 0
global total = 0

for n in 1:15
	stepval = (((sqrt(0.1)^n)/sqrt(factorial(n)))*(e^(-(abs(sqrt(0.1))^2)/2)))*n
	n = n+1
	global total = total + stepval
	println("Int Step:")
	println(n)
	println("Running total:")
	println(total)
end

print("Running probability:")
println(100-(total*100))
