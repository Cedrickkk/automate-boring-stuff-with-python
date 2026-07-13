def main():
    TB_CONVERSION_FACTOR = 1_000_000_000_000 / 1_099_511_627_776
    GB_CONVERSION_FACTOR = 1_000_000_000 / 1_073_741_824
    
    print("Enter TB or GB for the advertised unit: ")
    unit = input("> ")

    if unit.lower() == 'tb':
        discrepancy = TB_CONVERSION_FACTOR
    elif unit.lower() == 'gb':
        discrepancy = GB_CONVERSION_FACTOR
    else:
        raise ValueError(f"Unsupported unit: {unit}")

    print("Enter the advertised capacity: ")
    advertised_capacity = float(input("> "))

    real_capacity = calculate_dishonest_capacity(advertised_capacity, discrepancy)

    print(f"The actual capacity is {real_capacity} {unit}")
    
def calculate_dishonest_capacity(advertised_capacity: float, discrepancy: float) -> str:
    return str(round(advertised_capacity * discrepancy, 2))  

if __name__ == '__main__':
    main()