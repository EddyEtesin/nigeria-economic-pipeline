import schedule 
import time
import subprocess
from datetime import datetime

def run_pipeline():
    print("="* 40)
    print(f"Pipeline Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("\n Step 1: Extracting Data...")
    subprocess.run(["python", "extract.py"])

    print("\n Step 2: Transforming Data...")
    subprocess.run(["python", "transform.py"])

    print("\n Step 3: Loading Data...")
    subprocess.run(["python", "load.py"])

    print("\n" + "="*40)
    print(f"Pipeline complete: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 40)

if __name__ == "__main__":
    print("Scheduler started — pipeline will run every 24 hours")
    print(f"First run starting now: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run immediately on startup
    run_pipeline()
    
    # Then schedule to run every 24 hours
    schedule.every(24).hours.do(run_pipeline)
    
    while True:
        schedule.run_pending()
        time.sleep(60)