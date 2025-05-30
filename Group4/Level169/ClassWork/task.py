
if __name__ == '__main__':
    try:
        number = int(input("შეიყვანე მთელი რიცხვი: "))

        my_list = [1, 2, 3]
        print(my_list[number])

        result = 10 / number
        print("გაყოფის შედეგი:", result)

    except ValueError:
        print("შეიყვანე მხოლოდ რიცხვი!")

    except IndexError:
        print("მოცემული ინდექსი მასივის ზომაზე დიდია!")

    except ZeroDivisionError:
        print("ნულზე გაყოფა არ შეიძლება!")

    except Exception as e:
        print("წარმოიშვა გაუთვალისწინებელი შეცდომა:", e)
