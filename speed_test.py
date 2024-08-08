import speedtest

def main():
    try:
        # Create an instance of Speedtest
        speed_test = speedtest.Speedtest()

        # Get the best server based on ping
        speed_test.get_best_server()

        # Perform download speed test
        download_speed = speed_test.download()
        download_speed_mbps = download_speed / 1_000_000  # Convert to Mbps
        print(f"Your Download speed is: {download_speed_mbps:.2f} Mbps")

        # Perform upload speed test
        upload_speed = speed_test.upload()
        upload_speed_mbps = upload_speed / 1_000_000  # Convert to Mbps
        print(f"Your Upload speed is: {upload_speed_mbps:.2f} Mbps")

    except Exception as e:
        print("An error occurred during the speed test:", str(e))

if __name__ == "__main__":
    main()
