# Birthday_Cake_Candles

def birthdayCakeCandles(arr):
    tallest_candles_count= 0

    talest_candle= max(arr)

    tallest_candles_count=arr.count(talest_candle)
    print(tallest_candles_count)


n=int(input()) # Enter how many candle you want

arr=list(map(int,input().split())) # Enter candles

if len(arr)!=n:
    print("Error")
else:
    birthdayCakeCandles(arr)