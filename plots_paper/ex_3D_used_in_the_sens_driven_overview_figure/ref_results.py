import chaospy as cp
import numpy as np

def test_function(x):
	x1 = x[0]
	x2 = x[1]
	x3 = x[2]

	a = 0.05
	b = 7

	test = np.sin(x1) + a*(np.sin(x2)**2) + b*(x3**4)*np.sin(x1)
	
	return test

if __name__ == '__main__':
	q = 16
	p = 10

	dim = 3

	in_distr = [cp.Uniform() for d in range(dim)]

	distr = cp.J(*in_distr)

	print('begin')

	nodes, weights 	= cp.generate_quadrature(q, distr, rule='G')
	poly 			= cp.orth_ttr(p, distr)

	func_eval = [test_function(node) for node in nodes.T]

	gpc_approx = cp.fit_quadrature(poly, nodes, weights, func_eval)

	expect = cp.E(gpc_approx, distr)
	varian = cp.Var(gpc_approx, distr)

	sobol_total = cp.Sens_t(gpc_approx, distr)
	sobol_local = cp.Sens_m(gpc_approx, distr)


	print(len(nodes.T))

	print(expect)
	print(varian)

	print(sobol_local)
	print(sobol_total)

	print(sobol_total - sobol_local)