def main():
    #open video file for reading 
    video_file = open('video_times.txt', 'r')

    # initialize an accumulator
    total = 0.0

    # Initialize a variable to keep count of the videos
    count = 0

    print("Here are the run times for the videos")

    # Get the values from the file and the total times
    for line in video_file:
        # convert a line to float
        run_time = float(line)
        # add 1 to the count
        count += 1
        # diplay the time
        print("Video #", count, ": ", run_time, sep='')
        # add the time to the total
        total += run_time

    #close the video file
    video_file.close()

    # print the total of the running times.
    print("The running total time is", total, "seconds.")

main()
