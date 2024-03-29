from adcmodel.data import load_adc_csv

def test_load_adc_csv():
    df = load_adc_csv("urn:uuid:e248467d-e1f9-4a32-9e38-a9b4fb17cefb")
    assert df is not None

def test_load_adc_csv_shape():
    df = load_adc_csv("urn:uuid:e248467d-e1f9-4a32-9e38-a9b4fb17cefb")
    assert df is not None
    assert (df.shape[0] == 17856) & (df.shape[1] == 6)