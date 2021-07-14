# y0ka1
# Made on July 18th, 2021

# This program simulates a Jayne-Cummings Quantum System using Julia and QuantumOptics

using QuantumOptics
b_spin = SpinBasis(1//2)
b_fock = FockBasis(200)
sp = sigmap(b_spin)
sm = sigmam(b_spin)
a = destroy(b_fock)
at = create(b_fock)
H = sp⊗a + sm⊗at
T = [0:0.01:50;]
ψ0 = spindown(b_spin) ⊗ coherentstate(b_fock, 6)
tout, ψt = timeevolution.schroedinger(T, ψ0, H)

using PyPlot
plot(tout, expect(1, sp*sm, ψt))
xlabel("Time")
ylabel("Spin excitation")
tight_layout()
savefig("composite.svg")
