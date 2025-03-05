def create_tuple(no,no1,no2):
    mi=min(no,no1,no2)
    ma=max(no,no1,no2)
    sum=no+no1+no2
    return (mi,ma,sum)



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))