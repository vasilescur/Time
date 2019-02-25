# Open files
raw_data = open('data_raw.csv', 'r')
clean_data = open('data_clean.csv', 'w')

# Output header
clean_data.write('activity,start,end,minutes\n')

# Process line by line
line = raw_data.readline()
while line:
    parts = line.strip().split(',')

    # Example: Study,11 M12 2018 01:40,11 M12 2018 02:43,63

    # Parse
    activity_type = parts[0]
    start_raw = parts[1]
    end_raw = parts[2]
    minutes = parts[3]

    # Decode start and end times
    start_parts = start_raw.split(' ')
    start_day = start_parts[0]
    start_month = start_parts[1][1:]    # Ignore 'M'
    start_year = start_parts[2]

    start_time = start_parts[3]

    # Same for end
    end_parts = end_raw.split(' ')
    end_day = end_parts[0]
    end_month = end_parts[1][1:]    # Ignore 'M'
    end_year = end_parts[2]

    end_time = end_parts[3]

    # Prepare the output format
    out_start_date = '{}-{}-{}'.format(start_year, start_month, start_day)
    out_end_date = '{}-{}-{}'.format(end_year, end_month, end_day)

    out_start_time = start_time
    out_end_time = end_time

    out_line = '{},{} {},{} {},{}\n'.format(
        activity_type,
        out_start_date,
        out_start_time,
        out_end_date,
        out_end_time,
        minutes
    )

    # Write to output file
    clean_data.write(out_line)

    # Get the next line
    line = raw_data.readline()

# Clean up
raw_data.close()
clean_data.close()
