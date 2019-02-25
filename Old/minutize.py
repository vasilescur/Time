import datetime

# Open files
data = open('data_clean.csv', 'r')
data_minutes = open('data_minutes.csv', 'w')

# Output header
data_minutes.write('date_time,activity\n')

# Skip header line
line = data.readline()

# Process line by line
line = data.readline()
while line:
    parts = line.strip().split(',')

    # Example: Study,2018-12-11 01:40,2018-12-11 02:43,63

    # Parse
    activity = parts[0]
    end_raw = parts[2]
    # Ignore end time
    minutes = int(parts[3])

    end_year = int(end_raw.split('-')[0])
    end_month = int(end_raw.split('-')[1])
    end_day = int(end_raw.split('-')[2].split(' ')[0])
    end_hour = int(end_raw.split(' ')[1].split(':')[0])
    end_minute = int(end_raw.split(' ')[1].split(':')[1])

    end = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute)

    current_time = end

    # Write all those minutes of time
    for x in range(minutes):    # Make sure not to count last minute twice
        out_line = '{},{}\n'.format(current_time.strftime("%Y-%m-%d %H:%M"), activity)

        # Go backwards one minute
        current_time -= datetime.timedelta(minutes = 1)

        data_minutes.write(out_line)


    # Get the next line
    line = data.readline()

# Clean up
data.close()
data_minutes.close()
