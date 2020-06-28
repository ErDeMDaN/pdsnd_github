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
    
    # TO DO: get user input for city (chicago, new york city, washington). 
    # HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("Enter the name of the city (Chicago, New York City, Washington) you want to list its details: ").lower()
        if city in ['chicago','new york city','washington']:
            break
        else:
            print("\nPlease type one of the these cities: Chicago, New York City or Washington\n")
    
    # TO DO: get user input for month (all, january, february, march, ... , june)
    
    while True:
        month = input("Enter the name of the month you want to list its details or enter \'all\' to deploy no month filter: ").lower()
        if month in ['january','february','march','april','may','june','all']:
            break
        else:
            print("\nPlease type one of the months name or 'all' for not using month filter \n")

    # TO DO: get user input for day of week (all, monday, tuesday, wednesday, ... sunday)
    
    while True:
        day = input("Enter the name of the day you want to list its details or enter 'all' to apply no day filter: ").lower()
        if day in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
            break
        else:
            print("\nPlease type one of the days name or 'all' for not using day filter \n")

    print('-'*40)
    return city, month, day


def station_stats(df):
    """Shows statistics of the most favourite stations and trips."""

    print('\nCalculating The Most Favourite Stations and Trips...\n')
    start_time = time.time()

    # TO DO: show the most frequently used start station
    most_frequent_start_station = df['Start Station'].mode()[0]
    print("Most Frequent Start Station: ",most_frequent_start_station)

    # TO DO: show the most frequently used end station
    most_frequent_end_station = df['End Station'].mode()[0]
    print("Most Frequent End Station: ",most_frequent_end_station)

    # TO DO: show the most frequently combining of start and end station trip
    df['comb_of_station'] = df['Start Station'] + ' & ' + df['End Station']
    most_frequently_comb_of_station = df['comb_of_station'].mode()[0]
    print("Most Frequently Combining of Station: ",most_frequently_comb_of_station)
    
    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)


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

    # convert the Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the list of the months to get the related int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to generate the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to generate the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def user_stats(df,city):
    """Shows statistics of bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Show counts of user kinds
    user_kinds = df['User Type'].value_counts()
    print('Counts of User Kinds:\n')
    print(user_kinds)

    if city != 'washington':
    # TO DO: Show counts of gender
        gender = df['Gender'].value_counts()
        print('\nCounts of Gender:\n')
        print(gender)

    # TO DO: Show earliest, latest and most common year of birth
        earliest_year_of_birth    = int(df['Birth Year'].min())
        latest_year_of_birth      = int(df['Birth Year'].max())
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print("\nEarliest Year of Birth: ",earliest_year_of_birth)
        print("Latest Year of Birth: ",latest_year_of_birth)
        print("Most Common Year of Birth: ",most_common_year_of_birth)
    
    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)


def time_stats(df):
    """Shows statistics of the most frequent travel times."""

    print('\nCalculating The Most Frequent Travel Times...\n')
    start_time = time.time()

    # TO DO: show the most frequent month
    most_frequent_month = df['month'].mode()[0]
    print('Most Frequent Month: ',most_frequent_month)
    
    # TO DO: show the most frequent day of week
    most_frequent_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day: ',most_frequent_day)
    
    # TO DO: show the most frequent start hour
    # extract hour data from the Start Time column to generate an hour column
    df['hour'] = df['Start Time'].dt.hour
    most_frequent_hour = df['hour'].mode()[0]
    print('Most Frequent Hour: ',most_frequent_hour)
    
    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Shows statistics of the sum and mean trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: show sum of travel time
    Sum_trip_duration = df['Trip Duration'].sum()
    print('Sum of Travel Time: %s seconds.' % Sum_trip_duration)

    # TO DO: show mean of travel time
    Mean_trip_duration = df['Trip Duration'].mean()
    print('Mean of Travel Time: %s seconds' % Mean_trip_duration)

    print("\nThis process took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df,city):
    """Shows raw data output of bikeshare."""
    index_df = 0
    if city != 'washington':
        end_column = 9
    else: end_column = 7
    
    # If user want to visualize raw data,it will display 5 lines of raw data and then ask the user same question.
    while True:

        raw_data_request = input("Do you want to visualize raw data ? (Yes or No): ").lower()
        if raw_data_request == 'yes' :
            print(df.iloc[ index_df : index_df+5 , 1 : end_column ])
            index_df += 5
            continue
        elif raw_data_request == 'no' :
            break
        else :
            print("\nPlease type 'Yes' or 'No'.\n")
            
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df,city)
        restart = input('\nWould you like to restart? Type yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
                main()