
# task 1

class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        arr = []
        integers_list = ''.join(map(str, integers_list))
        for num in digits_list:
            arr.append((num, integers_list.count(str(num))))
        return arr
    
l = List()

integers_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
digits_list = [1, 3]

print(l.count_spec_digits(integers_list, digits_list))