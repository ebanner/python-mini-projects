if __name__ == '__main__':
    import pandas as pd
    df = pd.read_excel('sample_data.xlsx')
    print(df)
    df.to_excel('output_data.xlsx', index=False)
