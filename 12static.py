class Temperature_converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        result = (c * 9/5) + 32
        print(f"{c}C : {result}F")
        return result
Temperature_converter.celsius_to_fahrenheit(1)
