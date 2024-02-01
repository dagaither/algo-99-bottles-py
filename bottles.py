# make function sing_song that takes in an arg called num
# make function second_part
# make function for bottle/s

# make variable called first_part equal to first paragraph

def bottle_song(num):
    while num > 1:
        print(f"""{num} {bottles(num)} of beer on the wall, {num} {bottles(num)} of beer.\nTake one down and pass it around, {num-1} {bottles(num)} of beer on the wall.""")
        num -= 1
    if num > 0:
        print(f"""{num} {bottles(num)} of beer on the wall, {num} {bottles(num)} of beer.\nTake one down and pass it around, no more bottles of beer on the wall.""")
        num -= 1
    if num == 0:
        return (f"""No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.""")
    
def bottles(num):
    if num == 1:
        return "bottle"
    return "bottles"
    

print(bottle_song(99))