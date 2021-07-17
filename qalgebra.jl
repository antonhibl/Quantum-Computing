# y0ka1

# This program creates a framework to be used in the julia api as a quantum calculator

# Imports
import Plots
import LinearAlgebra
import MathPhysicalConstants

# Computational basis vectors
zero_state = [1;0]
one_state = [0;1]

# Gates

H = (1/sqrt(2))*[1 1;1 -1] # The Hadamard gate
I = [1 0;0 1] 		   # also U†*U=I
X = [0 1;1 0]       # Here it begins to become easy to see the symmetries
Y = [0 -im;im 0]   # An imaginary conjecture gate but quantum theory gives it many applications
Z = [1 0;0 -1]      # With Z the pauli gate are finished being described

# "super" matrixes are 4x4 matrixes of matrixes

super_H = (1/sqrt(2))*[[1 0;0 1] [0 1;1 0];[0 1;1 0] [-1 0;0 -1]]
super_Y = [zeros(2, 2) [0 -im;-im 0];[0 im;im 0] zeros(2, 2)]
super_Z = [[1 0;0 1] zeros(2, 2);zeros(2, 2) [-1 0;0 -1]]
super_I = [I zeros(2, 2);zeros(2, 2) I]
super_X = [zeros(2, 2) X;X zeros(2, 2)]
superlinearstate = [1 0 0 1; 0 0 0 0; 0 0 0 0; 0 1 1 0]


# Function and Matrix transforms

function Rotation(matrix, angle) # The matrix may also be a vector, the angle is more sensical in radians
    [cos(angle) -sin(angle);sin(angle) cos(angle)]+matrix
end

function SuperRotation(super_matrix, angle)
	[[cos(angle) cos(angle);cos(angle) cos(angle)] [-sin(angle) -sin(angle);-sin(angle) -sin(angle)];[cos(angle) cos(angle);cos(angle) cos(angle)] [sin(angle) sin(angle);sin(angle) sin(angle)]]+matrix
end

function Hermitian(matrix) # returns the hermitian of a matrix
    conj(transpose(matrix))
end

function C_NOT(vector1, vector2, direction)   # these should be two states and a specifier saying pos or neg
	if direction=="pos"
		((vector1+vector2)/sqrt(2))   #Theoretically we want it to entangle the states into one entangled state
	elseif direction=="neg"
		((vector1-vector2)/sqrt(2))
	else
		((vector1+vector2)/sqrt(2))
	end
end

