def number_to_words(n):
    if n == 0:
        return ""
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]
    
    def one_to_ninety_nine(n):
        if n < 10:
            return ones[n]
        elif n < 20:
            return teens[n-10]
        else:
            return tens[n//10] + ones[n%10]
    
    def one_to_nine_hundred_ninety_nine(n):
        if n < 100:
            return one_to_ninety_nine(n)
        else:
            return ones[n//100] + "hundred" + ("and" + one_to_ninety_nine(n%100) if n%100 != 0 else "")
    
    if n == 1000:
        return "onethousand"
    else:
        return one_to_nine_hundred_ninety_nine(n)

total_letters = sum(len(number_to_words(i)) for i in range(1, 1001))

print(total_letters)
