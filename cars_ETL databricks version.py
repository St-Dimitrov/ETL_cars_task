# Databricks notebook source
from pyspark.sql.functions import avg, desc

# COMMAND ----------

cars_account_key = dbutils.secrets.get(scope = 'cars-scope', key = 'cars-account-key')

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.carsdl.dfs.core.windows.net", 
    cars_account_key
)

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@carsdl.dfs.core.windows.net"))

# COMMAND ----------

cars_schema = "Acceleration DOUBLE, Cylinders BIGINT, Displacement DOUBLE, Horsepower BIGINT, Miles_per_Gallon DOUBLE, Name STRING, Origin STRING, Weight_in_lbs BIGINT, Year DATE"

# COMMAND ----------

cars_df = spark.read.schema(cars_schema).json("abfss://demo@carsdl.dfs.core.windows.net/cars.json")

# COMMAND ----------

display(cars_df.printSchema())

# COMMAND ----------

unique_cars = cars_df.select("Name").distinct().count()

# COMMAND ----------

avg_hp = cars_df.select(avg("Horsepower")).first()[0]

# COMMAND ----------

top_heavy_cars = cars_df.orderBy(desc("Weight_in_lbs")).limit(5)

# COMMAND ----------

cars_by_year = cars_df.groupBy("Year").count().orderBy("Year")

# COMMAND ----------

cars_by_manufacturer_origin = cars_df.groupBy("Origin").count().orderBy(desc("count"))

# COMMAND ----------

display(cars_by_manufacturer_origin)

# COMMAND ----------

cars_df.write.csv("abfss://demo@carsdl.dfs.core.windows.net/car_dataset.csv", header=True, mode="overwrite")

# COMMAND ----------


