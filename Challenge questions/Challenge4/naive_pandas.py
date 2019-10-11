import pandas as pd

def transpose_csv(input_file, output_file, header):
    data = pd.read_csv(input_file, header=header)
    data.T.to_csv(output_file, header=header, index=False)
