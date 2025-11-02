import numpy as np
import pandas as pd
import random
 

def generate_synthetic_data(num_samples=2000):
    """
    Generates synthetic adaptive learning data for training the Random Forest model.
    
    Features:
    - current_difficulty: 0 (Easy), 1 (Medium), 2 (Hard)
    - accuracy_last_5: Accuracy ratio in the last 5 problems.
    - time_ratio_avg: Average Time Taken / Average Time Threshold (Fluency metric).
    
    Target:
    - success_on_next_level: Will the user succeed at the next difficulty level? (1: Yes, 0: No)
    """

    data = {
        # Feature 1: Current Difficulty
        'current_difficulty': np.random.randint(0, 3, num_samples),
        
        # Feature 2: Accuracy Streak (using Beta distribution for biased accuracy)
        'accuracy_last_5': np.random.beta(a=5, b=2, size=num_samples), 
        
        # Feature 3: Fluency Ratio. Values < 1 mean fast; values > 1 mean slow.
        'time_ratio_avg': np.random.lognormal(mean=0.0, sigma=0.4, size=num_samples), 
    }
    
    df = pd.DataFrame(data)

    # Clamp the accuracy to be between 0.0 and 1.0
    df['accuracy_last_5'] = np.clip(df['accuracy_last_5'], 0.0, 1.0)

    # ----------------------------------------------------------------------
    # GENERATING THE TARGET VARIABLE (Simulating Adaptive Logic)
    # The model learns to predict success based on these synthetic rules:
    # ----------------------------------------------------------------------
    
    df['prob_success'] = 0.5 # Baseline probability

    # Rule 1: High Mastery AND Fluency (Fast and Accurate) -> High chance of success at next level
    condition_mastery_and_fluent = (df['time_ratio_avg'] < 0.9) & (df['accuracy_last_5'] > 0.8)
    df.loc[condition_mastery_and_fluent, 'prob_success'] += 0.4 

    # Rule 2: Slow but Accurate (Needs Fluency Practice) -> Medium chance
    condition_slow_mastery = (df['time_ratio_avg'] > 1.2) & (df['accuracy_last_5'] > 0.7)
    df.loc[condition_slow_mastery, 'prob_success'] -= 0.1 

    # Rule 3: Low Accuracy (Struggling) -> Low chance
    condition_struggling = (df['accuracy_last_5'] < 0.4)
    df.loc[condition_struggling, 'prob_success'] -= 0.3 
    
    # Clip probability and add small noise for realism
    df['prob_success'] = np.clip(df['prob_success'] + np.random.normal(0, 0.05, num_samples), 0, 1)

    # Create the final Binary Target Variable (1 or 0)
    df['success_on_next_level'] = (df['prob_success'] > np.random.rand(num_samples)).astype(int)
    
    # Drop the intermediate probability column
    df = df.drop(columns=['prob_success'])
    
    return df

if __name__ == '__main__':
    # Generate 2000 samples
    training_data = generate_synthetic_data(num_samples=2000)
    
    # Save the data to a CSV file
    training_data.to_csv('adaptive_training_data.csv', index=False)
    
    print("✅ 2000 rows of synthetic training data saved to 'adaptive_training_data.csv'.")
    print("This data is ready to be used for training the Random Forest model.")