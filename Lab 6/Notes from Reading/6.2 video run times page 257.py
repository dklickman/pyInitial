def main():
    # get the number of videos
    num_videos = int(input("How many videos are in the project?"))

    # Open the files that stores the video times
    video_file = open('video_times.txt', 'w')

    # get the video's run time from the user
    print("Enter the running times for each video.")
    for count in range(1, num_videos + 1):
        run_time = float(input("Video #" + str(count) + ": "))
        video_file.write(str(run_time) + '\n')

    #close the file
    video_file.close()
    print("The times have been saved to video_times.txt")

main()
                         
