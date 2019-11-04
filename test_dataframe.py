'''
This program is for check and test input dataframe meets the specific
requirement. If it meet the requirement, the test function will return
true, else will return false.
'''

def test_create_dataframe(dataframe, names_list):
    '''
    This test used in homework2.
    Parameters: dataframe, list names_list
    Returns: True if meets all the test case, False if not
    '''
    if dataframe.columns.tolist() != names_list:
        return False
    type_list = dataframe.dtypes.tolist()
    for i in type_list:
        if i != type_list[0]:
            return False
    if dataframe.shape[0] < 10:
        return False
    return True

def test_column_type(dataframe):
    '''
    Test if every row of a column has same type accord with the
    type of this column.
    Parameters: dataframe
    Returns: True if meet the test, False if not
    '''
    columns_list = dataframe.columns.tolist()
    for i in range(len(columns_list)):
        type_i = type(dataframe[columns_list[i]][0])
        for j in range(len(dataframe[columns_list[i]])):
            if type(dataframe[columns_list[i]][j]) != type_i:
                return False
    return True

def test_has_nan(dataframe):
    '''
    Test if there are any column in the dataframe has nan values.
    Parameters: dataframe
    Returns: True if it has nan value, False if not
    '''
    for isnan in dataframe.isnull().any().tolist():
        if isnan:
            return True
    return False

def test_num_of_row(dataframe):
    '''
    Test if the number of rows in dataframe is more than or equal to 1
    Parameters: dataframe
    Returns: True if more than or equal to 1, False if not
    '''
    return dataframe.shape[0] >= 1
