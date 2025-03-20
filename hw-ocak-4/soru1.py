nums = list(int(input(f"{i+1}. sayıyı giriniz: ")) for i in range(5))

def find_max(nums):
    max_num = nums[0]
    for num in nums[1:]:
        if num > max_num:
            max_num = num
    return max_num

def find_min(nums):
    min_num = nums[0]
    for num in nums[1:]:
        if num < min_num:
            min_num = num
    return min_num

def find_avg(nums):
    return sum(nums) / len(nums)

def sum_nums(nums):
    total = 0
    for num in nums:
        total += num
    return total

print(f"En büyük sayı: {find_max(nums)}")
print(f"En küçük sayı: {find_min(nums)}")
print(f"Ortalama: {find_avg(nums)}")
print(f"Toplam: {sum_nums(nums)}")