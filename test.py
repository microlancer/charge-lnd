def calculate_ppm(ppm_min, ppm_avg, ppm_upper, ratio):
    if ratio < 0 or ratio > 1:
        raise ValueError("Ratio must be between 0 and 1 inclusive")

    if ratio < 0.5:
        ppm = ppm_upper + 2 * (ppm_avg - ppm_upper) * ratio
    elif ratio > 0.5:
        ppm = ppm_min + 2 * (ppm_avg - ppm_min) * (1 - ratio)
    else:
        ppm = ppm_avg

    return ppm

# Example usage:
ppm_min = 100
ppm_avg = 200
ppm_upper = 4000
ratio = 0.5

result = calculate_ppm(ppm_min, ppm_avg, ppm_upper, ratio)
print(result)
