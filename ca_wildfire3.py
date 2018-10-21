# Use the Azure Machine Learning data source package
from azureml.dataprep import datasource

# Use the Azure Machine Learning data collector to log various metrics
from azureml.logging import get_azureml_logger
logger = get_azureml_logger()

# This call will load the referenced data source and return a DataFrame.
# If run in a PySpark environment, this call returns a
# Spark DataFrame. If not, it will return a Pandas DataFrame.
df = datasource.load_datasource('ca_wildfire3.dsource')

# Remove this line and add code that uses the DataFrame
df.head(10)
