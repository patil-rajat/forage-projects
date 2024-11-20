import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    df = pd.read_csv(file)
    return df

def exercise_1(df):
    column_names = df.columns.tolist()
    print(column_names)

def exercise_2(df, k):
    print(df.head(k))

def exercise_3(df, k):
    df_sample = df.sample(n=k)
    print(df_sample)

def exercise_4(df):
    transaction_types = df['type'].unique().tolist()
    return transaction_types

def exercise_5(df):
    top_destinations = df['type'].value_counts().head(10)
    return top_destinations 

def exercise_6(df):
    fraud_transactions = df[df['isFraud'] == 1]
    return fraud_transactions

def exercise_7(df):
    distinctDest = df.groupby('nameOrig')['nameDest'].nunique()
    sorted = distinctDest.sort_values(ascending=False)
    output = sorted.reset_index(name='distinctDest')
    return output

def visual_1(df):
    def transaction_counts(df):
        counts = df['type'].value_counts()
        return counts
    
    def transaction_counts_split_by_fraud(df):
        count_sum = df.groupby('type')['isFraud'].sum()
        return count_sum

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar', color='blue')
    axs[0].set_title('Transaction types')
    axs[0].set_xlabel('Transaction types')
    axs[0].set_ylabel('Counts')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction types (fradulent)')
    axs[1].set_xlabel('Transaction types')
    axs[1].set_ylabel('Fraud count')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    return 'graphs done'

def visual_2(df):
    def query(df):
        return df[['amount', 'isFraud']]
    
    plot = query(df).plot.scatter(x='amount',y='isFraud', alpha=0.5)
    plot.set_title('Amount v isFraud')
    plot.set_xlim(left=df['amount'].min() - 100, right=df['amount'].max() + 100)
    plot.set_ylim(bottom=-0.1, top=1.1)
    return 'Amount v isFraud'

def exercise_custom(df):
    fraud_rate = df.groupby('type')['isFraud'].mean()
    plt.figure(figsize=(10, 6))
    fraud_rate.plot(kind='bar', color='blue')
    plt.title('Fraud rate by transaction type')
    plt.xlabel('transaction type')
    plt.ylabel('Fraud rate')
    plt.show()
    
def visual_custom(df):
    exercise_custom(df)
