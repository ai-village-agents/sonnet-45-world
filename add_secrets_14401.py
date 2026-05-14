secrets = []
for i in range(14401, 14451):
    x = -5000 + ((i * 137) % 10000)
    y = -5000 + ((i * 193) % 10000)
    secrets.append(f"{{x:{x},y:{y},id:{i}}}")

# Print the block of secrets
print(",".join(secrets))
