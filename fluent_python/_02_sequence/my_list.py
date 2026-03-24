symbols = '$¢£¥€¤'

codes = []

for symbol in symbols:
    print(symbol)
    print(ord(symbol))
    codes.append(ord(symbol))

print(codes)

print('-'*80)
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

