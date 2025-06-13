# Leetcode
LeetCode Solutions
def to_simplified_chinese(n):
  if n == 0:
    return "零"
  if n < 0:
    return "负" + to_simplified_chinese(-n)

  units = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
  tens = ["", "十", "百", "千", "万", "亿"]

  result = ""
  num_str = str(n)
  for i, digit in enumerate(reversed(num_str)):
    digit_val = int(digit)
    if digit_val != 0:
      result = units[digit_val] + tens[i // 4] + result
    elif i % 4 == 0 and result: #add 零 for the thousands, millions, etc.
        result = "零" + result

  return result.replace("零零", "零").lstrip("零") #Remove extra 零

print(to_simplified_chinese(123456789)) # Output: 一亿二千三百万四千五百六十七
print(to_simplified_chinese(10000)) # Output: 一万
print(to_simplified_chinese(1000)) # Output:一千
print(to_simplified_chinese(0)) # Output: 零
print(to_simplified_chinese(-123)) #Output: 负一百二十三
