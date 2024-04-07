# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER
#
#    >= 30             >= 90             Hot and Humid
#    >= 30              < 90             Hot
#     <30              >= 90             Cool and Humid
#     <30               <90              Cool


def weather_check(temp, hum):
    if temp >= 30 and hum >= 90:
        return "Hot and Humid"
    elif temp >= 30 and hum < 90:
        return "Hot"
    elif temp < 30 and hum >= 90:
        return "Cool and Humid"
    else:
        return "Cool"


def main():
    while True:
        try:
            temperature = int(input("Enter temperature : "))
            humidity = int(input("Enter Humidity : "))
            break
        except ValueError:
            print("Please enter valid number!!!")

    value = weather_check(temperature, humidity)

    print(f"The weather is {value}")


if __name__ == "__main__":
    main()

