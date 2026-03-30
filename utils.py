import pandas as pd
import numpy as np
from datetime import datetime
from geopy.geocoders import Nominatim
from sklearn.preprocessing import MinMaxScaler

# Zodiac signs based on month and day
def get_zodiac_sign(month, day):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquarius'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Pisces'
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Taurus'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gemini'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Cancer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leo'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgo'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Scorpio'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagittarius'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Capricorn'
    return 'Unknown'

# Get latitude and longitude from place name
def get_coordinates(place):
    geolocator = Nominatim(user_agent="astrology_app")
    try:
        location = geolocator.geocode(place)
        if location:
            return location.latitude, location.longitude
        else:
            return 0.0, 0.0  # Default if not found
    except:
        return 0.0, 0.0

# Preprocess user input
def preprocess_input(dob, tob, place):
    # Parse date and time
    dob_dt = datetime.strptime(dob, '%Y-%m-%d')
    tob_dt = datetime.strptime(tob, '%H:%M')
    
    year = dob_dt.year
    month = dob_dt.month
    day = dob_dt.day
    hour = tob_dt.hour
    minute = tob_dt.minute
    
    lat, lon = get_coordinates(place)
    
    # Simulate planetary positions
    np.random.seed(year + month + day + hour + minute)
    planetary_positions = np.random.uniform(0, 360, 9)
    
    # Zodiac
    zodiac = get_zodiac_sign(month, day)
    zodiac_map = {'Aries':0, 'Taurus':1, 'Gemini':2, 'Cancer':3, 'Leo':4, 'Virgo':5, 'Libra':6, 'Scorpio':7, 'Sagittarius':8, 'Capricorn':9, 'Aquarius':10, 'Pisces':11}
    zodiac_num = zodiac_map.get(zodiac, 0)
    
    # Features: same as dataset
    features = [year, month, day, hour, minute, lat, lon, zodiac_num] + list(planetary_positions)
    
    return features, zodiac

# Load and preprocess dataset
def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    
    # Parse dates
    df['dob_dt'] = pd.to_datetime(df['dob'])
    df['year'] = df['dob_dt'].dt.year
    df['month'] = df['dob_dt'].dt.month
    df['day'] = df['dob_dt'].dt.day
    df['tob_dt'] = pd.to_datetime(df['tob'], format='%H:%M')
    df['hour'] = df['tob_dt'].dt.hour
    df['minute'] = df['tob_dt'].dt.minute
    
    # Get coordinates (simulate or use geopy, but for dataset, assume lat/lon are in place? Wait, place is string, but in csv it's city name)
    # For simplicity, since dataset has place as string, but no lat/lon, I'll simulate lat/lon based on place hash or something
    # But to make it simple, add lat/lon columns by simulating
    np.random.seed(42)
    df['lat'] = np.random.uniform(-90, 90, len(df))
    df['lon'] = np.random.uniform(-180, 180, len(df))
    
    # Zodiac
    df['zodiac'] = df.apply(lambda row: get_zodiac_sign(row['month'], row['day']), axis=1)
    zodiac_map = {'Aries':0, 'Taurus':1, 'Gemini':2, 'Cancer':3, 'Leo':4, 'Virgo':5, 'Libra':6, 'Scorpio':7, 'Sagittarius':8, 'Capricorn':9, 'Aquarius':10, 'Pisces':11}
    df['zodiac_num'] = df['zodiac'].map(zodiac_map)
    
    # Features: year, month, day, hour, minute, lat, lon, zodiac_num, sun_pos, ..., neptune_pos
    feature_cols = ['year', 'month', 'day', 'hour', 'minute', 'lat', 'lon', 'zodiac_num'] + [f'{p}_pos' for p in ['sun', 'moon', 'mars', 'mercury', 'jupiter', 'venus', 'saturn', 'uranus', 'neptune']]
    X = df[feature_cols].values
    
    # Normalize
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Reshape for RNN: (samples, timesteps=1, features)
    X_reshaped = X_scaled.reshape(X_scaled.shape[0], 1, X_scaled.shape[1])
    
    # Targets
    y = df[['marriage_age', 'job_success', 'financial_score']].values
    
    return X_reshaped, y, scaler