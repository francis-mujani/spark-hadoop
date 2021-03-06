from pyspark.sql import SparkSession



def init_spark():
    spark = SparkSession.builder.appName("helloword").getOrCreate()
    sc = spark.sparkContext
    return spark, sc



def main():
    spark, sc = init_spark()
    nums = sc.parallelize([1,2,3,4])
    print(nums.map(lambda x: x*x).collect())



if __name__ == '__main__':
    main()


# ./bin/spark-submit --master spark://10.20.0.3:7077 pyspark_code/spark_hello.py