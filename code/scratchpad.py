from draftkings import get_past_leaderboards, upload_parquet_s3


# data = get_past_leaderboards("2022-11-17", "2022-12-01")
import glob

upload_parquet_s3("data/parquet/leaderboards/2022-11-07/*")