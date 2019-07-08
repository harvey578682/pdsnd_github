import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try :
            city = input("Please input the city: ").lower()
            if city in ['chicago', 'new york city', 'washington']:
                break
            else:
                print("city not found!")
        
        except Exception:
            print("It's not a valid input!")

    # get user input for month (all, january, february, ... , june)
    while True:
        try :
            month = input("Please input the month: ").lower()
            if month in ['all', 'january', 'february','march','april','may','june']:
                break
            else:
                print("month not found!")
            
        except Exception:
            print("It's not a valid input!")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try :
            day = input("Please input the day of the week: ").lower()
            if day in ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']:
                break
            else:
                print("month not found!")
            
        except Exception:
            print("It's not a valid input!")
    print('-'*40)
    return city, month, day      


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)

    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day of week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day of week'].mode()[0]
    print('Most Common Day of Week:', popular_day_of_week)

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['stastions'] = df['Start Station'] + ", " +df['End Station']
    popular_stations = df['stastions'].mode()[0]
    print('Most popular trip from start to end:', popular_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time: {} s'.format(total_travel_time))

    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time: {} s'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ')
    print('{}: {}, {}: {}\n'.format(user_types.index[0], user_types[0] ,user_types.index[1], user_types[1]))


    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('Counts of gender: ')
        print('{}: {}, {}: {}\n'.format(gender.index[0], gender[0] ,gender.index[1], gender[1]))
    
    except Exception:
        print('No gender data\n')
        
    # Display earliest, most recent, and most common year of birth
    try:
        eariest_year_birth = int(df['Birth Year'].min())
        most_recent_year_birth = int(df['Birth Year'].max())
        most_common_year_birth = int(df['Birth Year'].mode()[0])
        print('Oldest, Youngest, and Most Popular Birth of Year:')
        print(eariest_year_birth, most_recent_year_birth, most_common_year_birth)
    
    except Exception:
        print('No Birth Year data')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(city):
    """Displays raw data on bikeshare users."""
    df = pd.read_csv(CITY_DATA[city])
    display = input('Do you want to see raw data? Enter yes or no.\n')
    print(df[0 : 5])
    i = 5
    if display == 'yes':
        while True:
            display_repeat = input('Do you want to see more 5 lines of raw data? Enter yes or no.\n')
            if display_repeat == 'yes':
                print(df[i : i + 5])
                i += 5
            else:
                break
    else:
        pass
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
