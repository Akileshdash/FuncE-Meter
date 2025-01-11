# Define lists for storing energy values
pkg_0 = []
pkg_1 = []
dram_0 = []
dram_1 = []

# Open and read the file
with open('values.txt', 'r') as file:
    # Skip the header line
    next(file)
    
    # Process each line
    for line in file:
        # Split the line into components
        domain, energy, duration = line.strip().split(',')
        
        # Convert energy to an integer
        energy = int(energy)
        
        # Append energy values to the respective lists
        if domain == "package-0":
            pkg_0.append(energy)
        elif domain == "package-1":
            pkg_1.append(energy)
        if domain == "dram-0":
            dram_0.append(energy)
        elif domain == "dram-1":
            dram_1.append(energy)
        # elif domain.startswith("dram"):  # Includes dram-0 and dram-1
        #     dram.append(energy)
print("pkg_0: ", pkg_0)
print("pkg_1: ", pkg_1)
print("dram_0: ", dram_0)
print("dram_1: ", dram_1)

# Calculate averages for each domain
avg_pkg_0 = sum(pkg_0)*1e-6 / len(pkg_0) if pkg_0 else 0
avg_pkg_1 = sum(pkg_1)*1e-6 / len(pkg_1) if pkg_1 else 0
avg_dram_0 = sum(dram_0)*1e-6 / len(dram_0) if dram_0 else 0
avg_dram_1 = sum(dram_1)*1e-6 / len(dram_1) if dram_1 else 0

# Print the results
print(f"Average energy for package-0: {avg_pkg_0} microjoules")
print(f"Average energy for package-1: {avg_pkg_1} microjoules")
print(f"Average energy for dram-0: {avg_dram_0} microjoules")
print(f"Average energy for dram-1: {avg_dram_1} microjoules")
print("\n")
print(f"Total Package Energy: {sum(pkg_0)*1e-6 + sum(pkg_1)*1e-6} joules")
print(f"Total Dram Energy: {sum(dram_0)*1e-6 + sum(dram_1)*1e-6} joules")
print("\n")
print(f"Total Package Energy: {sum(pkg_0)*1e-7 + sum(pkg_1)*1e-7} joules")
print(f"Total Dram Energy: {sum(dram_0)*1e-7 + sum(dram_1)*1e-7} joules")