if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    return (data.loc[((data.passenger_count > 0) & (data.trip_distance >0)), ]
                .assign(lpep_pickup_date=lambda x: x['lpep_pickup_datetime'].dt.date)
                .rename(
                    columns={
                        'VendorID': 'vendor_id',
                        'RatecodeID': 'ratecode_id',
                        'PULocationID': 'pu_location_id',
                        'DOLocationID': 'do_location_id',
                    }
                )
    )


@test
def test_column_values(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert (output['passenger_count'] > 0).all() , 'The output had values =< 0 in column \'passenger_count\''
    assert (output['trip_distance'] > 0).all() , 'The output had values =< 0 in column \'trip_distance\''

@test
def test_vendor_id(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['vendor_id'].dropna().isin([1, 2]).all() , 'The output had values =< 0 in column \'passenger_count\''