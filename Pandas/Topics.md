# Pandas Learning Roadmap

## 1. Introduction to Pandas

- **What is Pandas?**
- **Installation**: `pip install pandas`
- **Basic Data Structures**: Series and DataFrame

## 2. Data Structures

- **Series**: One-dimensional labeled array capable of holding any data type.
- **DataFrame**: Two-dimensional labeled data structure with columns of potentially different types.

## 3. DataFrame Basics

- **Creating DataFrames**: From dictionaries, lists, and other data structures.
- **Viewing Data**: `head()`, `tail()`, `info()`, `describe()`
- **Selection and Indexing**: `loc`, `iloc`, boolean indexing

## 4. Data Manipulation

- **Handling Missing Data**: `isnull()`, `dropna()`, `fillna()`
- **Data Cleaning**: Removing duplicates, replacing values
- **Data Transformation**: Applying functions, mapping, and applying custom functions with `apply()`

## 5. Data Aggregation and Grouping

- **GroupBy**: Splitting, applying, and combining data
- **Aggregation Functions**: `sum()`, `mean()`, `count()`, `min()`, `max()`

## 6. Merging and Joining

- **Concatenation**: `concat()`
- **Merging**: `merge()`
- **Joining**: `join()`

## 7. Data Input and Output

- **Reading Data**: `read_csv()`, `read_excel()`, `read_sql()`, `read_json()`
- **Writing Data**: `to_csv()`, `to_excel()`, `to_sql()`, `to_json()`

## 8. Time Series Analysis

- **Date and Time Data**: `to_datetime()`, `date_range()`
- **Resampling**: `resample()`
- **Time Shifts**: `shift()`, `tshift()`

## 9. Visualization

- **Basic Plotting**: `plot()`
- **Integration with Matplotlib**: Customizing plots

## Key Methods and Functions

### DataFrame Creation

- `pd.DataFrame()`
- `pd.Series()`

### Viewing Data

- `df.head()`
- `df.tail()`
- `df.info()`
- `df.describe()`

### Selection and Indexing

- `df.loc[]`
- `df.iloc[]`
- `df[df['column'] > value]`

### Handling Missing Data

- `df.isnull()`
- `df.dropna()`
- `df.fillna()`

### Data Cleaning

- `df.drop_duplicates()`
- `df.replace()`

### Data Transformation

- `df.apply()`
- `df.map()`

### Grouping and Aggregation

- `df.groupby()`
- `df.agg()`

### Merging and Joining

- `pd.concat()`
- `pd.merge()`
- `df.join()`

### Input and Output

- `pd.read_csv()`
- `pd.read_excel()`
- `df.to_csv()`
- `df.to_excel()`

### Time Series

- `pd.to_datetime()`
- `pd.date_range()`
- `df.resample()`
- `df.shift()`

### Visualization

- `df.plot()`

## Additional Resources

- **Documentation**: [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- **Tutorials**: Websites like W3Schools, GeeksforGeeks, and official Pandas tutorials.
- **Books**: "Python for Data Analysis" by Wes McKinney (creator of Pandas)

## Practical Application

From your workflow, it looks like you have a file named `CleaningData.csv` and a Jupyter notebook `Practic.ipynb`. You can start by loading the CSV file into a DataFrame and performing basic operations like viewing the data, cleaning it, and performing some analysis.
