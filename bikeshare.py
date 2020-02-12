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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Which city do you want to explore? Please enter 'Chicago', 'New York City' or 'Washington'. ").lower().strip()
        print()
        if city in ['chicago','new york city','washington']:
            break
        print("Sorry, I did not understand your answer.")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("In which month are you interested ? \nPlease enter the month you are "\
                      "interested in ('January' or 'February'... ) you can also enter 'all' for "\
                     "all months \n").lower().strip()
        print()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                     'september', 'october', 'november', 'december', 'all']:
            break
        print("Sorry, I did not understand your answer.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day = input("In which day of the week are you interested ? \nPlease enter the day you are "\
                      "interested in ('Monday' or 'Tuesday'... ) you can also enter 'all' for "\
                     "all days \n").lower().strip()
       if day in ['monday','tuesday', 'wednesday','thursday','friday','saturday','sunday', 'all']:
           break
       print("Sorry, I did not understand your answer.")

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
    print('most common start month:')
    print(months[(pd.to_datetime(df['Start Time']).dt.month).mode()[0]].title())

    # TO DO: display the most common day of week
    print('most common day of the week')
    print((pd.to_datetime(df['Start Time']).dt.weekday_name).mode()[0])


    # TO DO: display the most common start hour
    print('most common start hour:')
    print((pd.to_datetime(df['Start Time']).dt.hour).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most frequent start station:')
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('most frequent end station:')
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination:')
    combi = df['Start Station'] + ' || ' +df['End Station']
    print(combi.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time:')
    print((pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum() )

    # display mean travel time
    print('mean travel time:')
    print((pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean() )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types')
    print(df['User Type'].value_counts())

    # Display counts of gender
    try:
        print('counts of gender')
        print(df['Gender'].value_counts())
    except:
        print('There is no gender data available for this city.')
    # Display earliest, most recent, and most common year of birth
    try:
        print('earliest birth year')
        print(int(df['Birth Year'].min()))
        print('most recent birth year')
        print(int(df['Birth Year'].max()))
        print('Most common birth year')
        print(int(df['Birth Year'].mode()[0]))
    except:
        print('There is no birth year data available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df, start):
    # Display 5 rows starting with the index 'start'
    for i in range(5):
        print(df.iloc[start+i])
        print('\n')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        srt_ind = 0
        #Let the possibility of displaying raw data
        while True:
            raw = input('\nWould you like to see raw data ? Enter yes or no.\n')
            if 'n' in raw:
                break
            display_raw(df, srt_ind)
            srt_ind += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
