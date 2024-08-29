## Categorical Variable

_There are two types of categorical variable._

- `Nominal`
- `Ordinal`

## Nominal

_In nominal the data is like male, female, red, green and like town name. We can not use normal string encoding like convert male into 1 and female into 0. In that case might be our algorithm take that in male > female or female > male._

## Ordinal

_In ordinal the data is like high, medium, low, master, phd, neutral. We can use normal encoding like low is 0, medium is 1 and hight is 2._

## One hot encoding

_To solve the nominal, we use one hot encoding. We make separate column for each label like red, green, blue and assign binary value 1 and 0.The extra variable created in this process is known as `dummy_variables`._
