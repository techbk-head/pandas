import os
for root, dirs, files in os.walk('/home/thang/Desktop'):
    for file in files:
        if file.endswith('n-'):
            print file