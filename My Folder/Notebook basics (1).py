# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 'Hello World from SQL notebook'

# COMMAND ----------

# MAGIC %md
# MAGIC # Markdown Title
# MAGIC ## Markdown Title 2
# MAGIC ### Markdown Title 3
# MAGIC 
# MAGIC text in **bold** and *italicized*
# MAGIC 
# MAGIC ordered list
# MAGIC 1. apples
# MAGIC 1. Pears 
# MAGIC 1. Strawberries
# MAGIC 
# MAGIC unordered list
# MAGIC * apples
# MAGIC * Pears 
# MAGIC * Strawberries
# MAGIC 
# MAGIC Table
# MAGIC |fruit| vendor    |
# MAGIC |-----| ----------|
# MAGIC |apple| Tesco     |
# MAGIC |pears| Aldi      |
# MAGIC 
# MAGIC 
# MAGIC Image
# MAGIC 
# MAGIC Links

# COMMAND ----------

# MAGIC %run ./includes/setup

# COMMAND ----------

print (full_name)

# COMMAND ----------

# MAGIC %fs ls /'databricks-datasets'

# COMMAND ----------



# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets')
display (files)

# COMMAND ----------


