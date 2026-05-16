import numpy as np
import matplotlib.pyplot as plt

def simulate_drift(N_individuals, generations, runs, initial_p=0.5):
    """
    Simulates genetic drift using the Wright-Fisher model.
    N_individuals: Number of diploid individuals (2N alleles)
    """
    final_frequencies = []
    alleles = 2 * N_individuals
    
    for _ in range(runs):
        p = initial_p
        for _ in range(generations):
            # Draw the next generation's allele count from a binomial distribution
            A1_count = np.random.binomial(alleles, p)
            p = A1_count / alleles
        
        # Round to the nearest 0.05 as requested by the assignment
        rounded_p = round(p * 20) / 20
        final_frequencies.append(rounded_p)
        
    return final_frequencies

# Run parameters
generations = 20
runs = 50

# Part a: Census size N=16
freqs_16 = simulate_drift(16, generations, runs)

# Part b: Effective size N=9
freqs_9 = simulate_drift(9, generations, runs)

# --- Plotting the Histograms Separately ---
bins = np.arange(-0.025, 1.075, 0.05) # Centered bins for 0.0, 0.05, 0.10, etc.

# First Graph: N=16
plt.figure(figsize=(8, 5))
plt.hist(freqs_16, bins=bins, edgecolor='black', color='skyblue')
plt.title("Part A: Final Frequencies after 20 Generations (N = 16)")
plt.xlabel("Final frequency of allele A1")
plt.ylabel("Number of runs")
plt.xlim(-0.05, 1.05)
plt.xticks(np.arange(0, 1.1, 0.1))
plt.grid(True)
plt.tight_layout()
plt.show() # Displays the first graph

# Second Graph: N=9
plt.figure(figsize=(8, 5))
plt.hist(freqs_9, bins=bins, edgecolor='black', color='salmon')
plt.title("Part B: Final Frequencies after 20 Generations (N = 9)")
plt.xlabel("Final frequency of allele A1")
plt.ylabel("Number of runs")
plt.xlim(-0.05, 1.05)
plt.xticks(np.arange(0, 1.1, 0.1))
plt.tight_layout()
plt.show() # Displays the second graph