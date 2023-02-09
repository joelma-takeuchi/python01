import sys, antigravity

def validate_inputs():
    if len(sys.argv) != 4:
        print("This program must have 3 arguments: Latitude, Longitude and DateRow")
        return False
    else:
        return True
    
def main():
    if validate_inputs():
        try:
            antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), str(sys.argv[3]).encode('utf-8'))
        except:
            print("This program must have 3 arguments: Latitude, Longitude and DateRow")

if __name__ == '__main__':
    main()