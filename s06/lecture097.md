# Data Analysis with pandas

```python
pip install pandas
```

## Getting started

```bash
> ipython
```

```python
> import pandas
> df1=pandas.DataFrame([[2,4,6],[10,20,30]])
> df1

out:
   0  1  2
0  2  4  6
1 10 20 30

> df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price", "Age", "Value"])
> df1

out:
   Price  Age  Value
0      2    4      6
1     10   20     30

> df1 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price", "Age","Value"],index=["First", "Second"])
> df1

out:
        Price  Age  Value
First       2    4      6
Second     10   20     30

> df2=pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])
> df2

Out:
   Name
0  John
1  Jack

> df2=pandas.DataFrame([{"Name":"John", "Surname":"Johns"},{"Name":"Jack"}])
> df2

Out:
   Name Surname
0  John   Johns
1  Jack     NaN

> dir(df1) # lists all the methods of the DataFrame object

> df1.Price

Out:
First      2
Second    10
Name: Price, dtype: int64

> df1.Price.mean()

Out: 6.0

> df1.Price.max()

Out: 10
```