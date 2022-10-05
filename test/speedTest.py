import speedtest

st = speedtest.Speedtest()

while True:
    download_speed = st.download()

    print('Download Speed: {:5.2f} Mb'.format(downlo0ad_speed/(1024*1024)))